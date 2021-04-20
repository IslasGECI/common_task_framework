from os import path
from pathlib import Path
import numpy as np
import pandas as pd


class Referee:
    def __init__(self, path_to_complete_dataset: str):
        self.path_to_complete_dataset = path_to_complete_dataset
        self.data = self.load_complete_dataset()

    def load_complete_dataset(self):
        data = pd.read_csv(self.path_to_complete_dataset)
        return data

    def get_training_length(self):
        total_length = len(self.data)
        training_proportion = 0.8
        training_length = round(total_length * training_proportion)
        return training_length

    def get_testing_length(self):
        total_length = len(self.data)
        training_length = self.get_training_length()
        testing_length = total_length - training_length
        return testing_length

    def get_training_dataset(self):
        training_length = self.get_training_length()
        train = self.data.head(training_length)
        return train

    def get_testing_dataset(self):
        testing_length = self.get_testing_length()
        test = self.data.iloc[-testing_length:, self.data.columns != "target"]
        return test

    def get_example_submission(self):
        testing_length = self.get_testing_length()
        example_submission = self.data.iloc[-testing_length:, self.data.columns == "id"]
        example_submission["target"] = np.random.rand(testing_length)
        return example_submission

    def get_behind_the_wall_solution(self):
        testing_length = self.get_testing_length()
        solution = self.data[["id", "target"]].tail(testing_length)
        return solution

    def get_training_path(self):
        directory = str(Path(self.path_to_complete_dataset).parents[0])
        training_path = path.join(directory, "train.csv")
        return training_path

    def get_testing_path(self):
        directory = str(Path(self.path_to_complete_dataset).parents[0])
        testing_path = path.join(directory, "test.csv")
        return testing_path

    def get_example_submission_path(self):
        directory = str(Path(self.path_to_complete_dataset).parents[0])
        example_submission_path = path.join(directory, "example_submission.csv")
        return example_submission_path

    def save_training_dataset(self):
        training_dataset = self.get_training_dataset()
        path_to_training = self.get_training_path()
        training_dataset.to_csv(path_to_training, index=False)

    def save_testing_dataset(self):
        testing_dataset = self.get_testing_dataset()
        path_to_testing = self.get_testing_path()
        testing_dataset.to_csv(path_to_testing, index=False)

    def save_example_submission(self):
        example_submission = self.get_example_submission()
        path_to_example_submission = self.get_example_submission_path()
        example_submission.to_csv(path_to_example_submission, index=False)

    def init(self):
        self.save_training_dataset()
        self.save_testing_dataset()
        self.save_example_submission()


def load_submission(path_to_submision):
    submission = pd.read_csv(path_to_submision)
    return submission