# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SMTPNotificationRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'subject_template': 'str',
        'body_template': 'str',
        'to': 'str'
    }

    attribute_map = {
        'type': 'type',
        'subject_template': 'subjectTemplate',
        'body_template': 'bodyTemplate',
        'to': 'to'
    }

    def __init__(self, type=None, subject_template=None, body_template=None, to=None):  # noqa: E501
        """SMTPNotificationRule - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._subject_template = None
        self._body_template = None
        self._to = None
        self.discriminator = None

        self.type = type
        self.subject_template = subject_template
        if body_template is not None:
            self.body_template = body_template
        self.to = to

    @property
    def type(self):
        """Gets the type of this SMTPNotificationRule.  # noqa: E501


        :return: The type of this SMTPNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SMTPNotificationRule.


        :param type: The type of this SMTPNotificationRule.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["smtp"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def subject_template(self):
        """Gets the subject_template of this SMTPNotificationRule.  # noqa: E501


        :return: The subject_template of this SMTPNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._subject_template

    @subject_template.setter
    def subject_template(self, subject_template):
        """Sets the subject_template of this SMTPNotificationRule.


        :param subject_template: The subject_template of this SMTPNotificationRule.  # noqa: E501
        :type: str
        """
        if subject_template is None:
            raise ValueError("Invalid value for `subject_template`, must not be `None`")  # noqa: E501

        self._subject_template = subject_template

    @property
    def body_template(self):
        """Gets the body_template of this SMTPNotificationRule.  # noqa: E501


        :return: The body_template of this SMTPNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._body_template

    @body_template.setter
    def body_template(self, body_template):
        """Sets the body_template of this SMTPNotificationRule.


        :param body_template: The body_template of this SMTPNotificationRule.  # noqa: E501
        :type: str
        """

        self._body_template = body_template

    @property
    def to(self):
        """Gets the to of this SMTPNotificationRule.  # noqa: E501


        :return: The to of this SMTPNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SMTPNotificationRule.


        :param to: The to of this SMTPNotificationRule.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SMTPNotificationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other