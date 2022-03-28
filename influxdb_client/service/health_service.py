# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from influxdb_client.service._base_service import _BaseService


class HealthService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """HealthService - a operation defined in OpenAPI."""
        if api_client is None:
            raise ValueError("Invalid value for `api_client`, must be defined.")
        self.api_client = api_client

    def get_health(self, **kwargs):  # noqa: E501,D401,D403
        """Get the health of an instance.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_health_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_health_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_health_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """Get the health of an instance.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_health_prepare(**kwargs)

        return self.api_client.call_api(
            '/health', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='HealthCheck',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_health_async(self, **kwargs):  # noqa: E501,D401,D403
        """Get the health of an instance.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_health_prepare(**kwargs)

        return await self.api_client.call_api(
            '/health', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='HealthCheck',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_health_prepare(self, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['zap_trace_span']  # noqa: E501
        self._check_operation_params('get_health', all_params, local_var_params)

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
