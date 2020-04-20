from tornado import gen

from db.base_methd import add, update


class BaseModel(object):
    """
    define a base model for base sql method and soft_delete column
    """

    def __init__(self):
        self._deleted = 0

    @property
    def deleted(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: int
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: int
        """

        self._deleted = deleted

    @gen.coroutine
    def save(self):
        """
        this method is a simple orm method for saving a object to the database
        and setting the object id property with an auto-generated id
        """

        self.id = add(self)

    @gen.coroutine
    def update(self):
        update(self)

    @gen.coroutine
    def soft_delete(self):
        self.deleted = 1
        update(self)
