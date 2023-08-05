import abc
from model.calculation.dataset.dataset import Dataset


class CalculationNode(metaclass=abc.ABCMeta):
    """Abstract base class for calculation nodes in a computational workflow.

    Attributes:
        data (dict): A dictionary containing data components of the dataset.
            This dictionary is shared among all instances of CalculationNode.

    Note:
        The `Dataset` class from `model.calculation.dataset.dataset` provides the `data` dictionary
        that holds the dataset components. The `data` attribute in CalculationNode is set as a reference
        to the `data` attribute in the Dataset class.
    """

    data = Dataset.data

    @abc.abstractmethod
    def execute(self):
        """Abstract method to be implemented by subclasses.

        This method represents the main execution logic for the calculation node.
        Subclasses need to override this method and provide the specific implementation.

        Raises:
            NotImplementedError: If the subclass does not provide an implementation.
        """
        pass
