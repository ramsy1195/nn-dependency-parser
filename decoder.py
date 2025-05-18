import sys
import copy

import numpy as np
import torch

from conll_reader import DependencyStructure, DependencyEdge, conll_reader
from extract_training_data import FeatureExtractor, State
from train_model import DependencyModel

class Parser(object):

    def __init__(self, extractor, modelfile):
        self.extractor = extractor

        # Create a new model and load the parameters
        self.model = DependencyModel(len(extractor.word_vocab), len(extractor.output_labels))
        self.model.load_state_dict(torch.load(modelfile))
        sys.stderr.write("Done loading model")

        # The following dictionary from indices to output actions will be useful
        self.output_labels = dict([(index, action) for (action, index) in extractor.output_labels.items()])

    def parse_sentence(self, words, pos):

        state = State(range(1,len(words)))
        state.stack.append(0)

        # TODO: Write the body of this loop for part 5
        while state.buffer:
            # Extract features from the current state
            features = self.extractor.get_input_representation(words, pos, state)
            print(f"Extracted features: {features}")


            # Make a prediction using the model
            with torch.no_grad():
                features_tensor = torch.tensor(features, dtype=torch.long).unsqueeze(0)

                action_probs = self.model(features_tensor)

                action_probs = torch.softmax(action_probs, dim=1).detach().numpy().flatten()
            print(f"Action probabilities: {action_probs}")

            # Create a list of possible actions based on the probabilities
            possible_actions = []
            for action_idx in range(len(action_probs)):
                action = self.output_labels[action_idx]
                possible_actions.append((action_probs[action_idx], action))

            # Sort possible actions by probability
            possible_actions.sort(reverse=True, key=lambda x: x[0])
            print(f"Possible actions (sorted): {possible_actions}")

            # Select the highest scoring permitted transition
            action_taken = False
            for _, action in possible_actions:
                if action[0] == 'shift' and len(state.stack) < 2:  # Cannot shift if only root is on the stack
                    continue
                elif action[0] == 'left_arc' and len(state.stack) > 1:  # Cannot arc-left if stack is empty
                    parent = state.stack[-1]
                    child = state.stack[-2]
                    state.deps.append((parent, child, 'label'))  # Replace 'label' with appropriate logic
                    state.stack.pop()
                    action_taken = True
                    print(f"Action taken: {action} (left arc) between {parent} and {child}")
                    break
                elif action[0] == 'right_arc' and len(state.stack) > 1:  # Cannot arc-right if stack is empty
                    child = state.stack.pop()
                    parent = state.stack[-1]
                    state.deps.append((parent, child, 'label'))  # Replace 'label' with appropriate logic
                    action_taken = True
                    print(f"Action taken: {action} (right arc) between {parent} and {child}")
                    break
                elif action[0] == 'shift':
                    state.stack.append(state.buffer.pop(0))
                    action_taken = True
                    print(f"Action taken: {action}, moving to stack: {state.stack}")
                    break

            print(f"Current state: Stack: {state.stack}, Buffer: {state.buffer}, Dependencies: {state.deps}")

            if not action_taken:
                print("No valid actions available, terminating parsing.")
                break


        result = DependencyStructure()
        for p, c, r in state.deps:
            result.add_deprel(DependencyEdge(c, words[c], pos[c], p, r))

        return result



if __name__ == "__main__":

    WORD_VOCAB_FILE = 'data/words.vocab'
    POS_VOCAB_FILE = 'data/pos.vocab'

    try:
        word_vocab_f = open(WORD_VOCAB_FILE,'r')
        pos_vocab_f = open(POS_VOCAB_FILE,'r')
    except FileNotFoundError:
        print("Could not find vocabulary files {} and {}".format(WORD_VOCAB_FILE, POS_VOCAB_FILE))
        sys.exit(1)

    extractor = FeatureExtractor(word_vocab_f, pos_vocab_f)
    parser = Parser(extractor, sys.argv[1])

    with open(sys.argv[2],'r') as in_file:
        for dtree in conll_reader(in_file):
            words = dtree.words()
            pos = dtree.pos()
            deps = parser.parse_sentence(words, pos)
            print(deps.print_conll())
            print()
