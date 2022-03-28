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


class ReplicationsService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """ReplicationsService - a operation defined in OpenAPI."""
        if api_client is None:
            raise ValueError("Invalid value for `api_client`, must be defined.")
        self.api_client = api_client

    def delete_replication_by_id(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_replication_by_id(replication_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_replication_by_id_with_http_info(replication_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_replication_by_id_with_http_info(replication_id, **kwargs)  # noqa: E501
            return data

    def delete_replication_by_id_with_http_info(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_replication_by_id_with_http_info(replication_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._delete_replication_by_id_prepare(replication_id, **kwargs)

        return self.api_client.call_api(
            '/api/v2/replications/{replicationID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def delete_replication_by_id_async(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a replication.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._delete_replication_by_id_prepare(replication_id, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/replications/{replicationID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _delete_replication_by_id_prepare(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['replication_id', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('delete_replication_by_id', all_params, local_var_params)
        # verify the required parameter 'replication_id' is set
        if ('replication_id' not in local_var_params or
                local_var_params['replication_id'] is None):
            raise ValueError("Missing the required parameter `replication_id` when calling `delete_replication_by_id`")  # noqa: E501

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replicationID'] = local_var_params['replication_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def get_replication_by_id(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replication_by_id(replication_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_replication_by_id_with_http_info(replication_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_replication_by_id_with_http_info(replication_id, **kwargs)  # noqa: E501
            return data

    def get_replication_by_id_with_http_info(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replication_by_id_with_http_info(replication_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_replication_by_id_prepare(replication_id, **kwargs)

        return self.api_client.call_api(
            '/api/v2/replications/{replicationID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replication',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_replication_by_id_async(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a replication.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_replication_by_id_prepare(replication_id, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/replications/{replicationID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replication',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_replication_by_id_prepare(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['replication_id', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('get_replication_by_id', all_params, local_var_params)
        # verify the required parameter 'replication_id' is set
        if ('replication_id' not in local_var_params or
                local_var_params['replication_id'] is None):
            raise ValueError("Missing the required parameter `replication_id` when calling `get_replication_by_id`")  # noqa: E501

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replicationID'] = local_var_params['replication_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def get_replications(self, org_id, **kwargs):  # noqa: E501,D401,D403
        """List all replications.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replications(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str name:
        :param str remote_id:
        :param str local_bucket_id:
        :return: Replications
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_replications_with_http_info(org_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_replications_with_http_info(org_id, **kwargs)  # noqa: E501
            return data

    def get_replications_with_http_info(self, org_id, **kwargs):  # noqa: E501,D401,D403
        """List all replications.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replications_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str name:
        :param str remote_id:
        :param str local_bucket_id:
        :return: Replications
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_replications_prepare(org_id, **kwargs)

        return self.api_client.call_api(
            '/api/v2/replications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replications',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def get_replications_async(self, org_id, **kwargs):  # noqa: E501,D401,D403
        """List all replications.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str org_id: The organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str name:
        :param str remote_id:
        :param str local_bucket_id:
        :return: Replications
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._get_replications_prepare(org_id, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/replications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replications',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _get_replications_prepare(self, org_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['org_id', 'zap_trace_span', 'name', 'remote_id', 'local_bucket_id']  # noqa: E501
        self._check_operation_params('get_replications', all_params, local_var_params)
        # verify the required parameter 'org_id' is set
        if ('org_id' not in local_var_params or
                local_var_params['org_id'] is None):
            raise ValueError("Missing the required parameter `org_id` when calling `get_replications`")  # noqa: E501

        path_params = {}

        query_params = []
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'remote_id' in local_var_params:
            query_params.append(('remoteID', local_var_params['remote_id']))  # noqa: E501
        if 'local_bucket_id' in local_var_params:
            query_params.append(('localBucketID', local_var_params['local_bucket_id']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def patch_replication_by_id(self, replication_id, replication_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_replication_by_id(replication_id, replication_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param ReplicationUpdateRequest replication_update_request: (required)
        :param str zap_trace_span: OpenTracing span context
        :param bool validate: If true, validate the updated information, but don't save it.
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_replication_by_id_with_http_info(replication_id, replication_update_request, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_replication_by_id_with_http_info(replication_id, replication_update_request, **kwargs)  # noqa: E501
            return data

    def patch_replication_by_id_with_http_info(self, replication_id, replication_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_replication_by_id_with_http_info(replication_id, replication_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param ReplicationUpdateRequest replication_update_request: (required)
        :param str zap_trace_span: OpenTracing span context
        :param bool validate: If true, validate the updated information, but don't save it.
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._patch_replication_by_id_prepare(replication_id, replication_update_request, **kwargs)

        return self.api_client.call_api(
            '/api/v2/replications/{replicationID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replication',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def patch_replication_by_id_async(self, replication_id, replication_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a replication.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str replication_id: (required)
        :param ReplicationUpdateRequest replication_update_request: (required)
        :param str zap_trace_span: OpenTracing span context
        :param bool validate: If true, validate the updated information, but don't save it.
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._patch_replication_by_id_prepare(replication_id, replication_update_request, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/replications/{replicationID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replication',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _patch_replication_by_id_prepare(self, replication_id, replication_update_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['replication_id', 'replication_update_request', 'zap_trace_span', 'validate']  # noqa: E501
        self._check_operation_params('patch_replication_by_id', all_params, local_var_params)
        # verify the required parameter 'replication_id' is set
        if ('replication_id' not in local_var_params or
                local_var_params['replication_id'] is None):
            raise ValueError("Missing the required parameter `replication_id` when calling `patch_replication_by_id`")  # noqa: E501
        # verify the required parameter 'replication_update_request' is set
        if ('replication_update_request' not in local_var_params or
                local_var_params['replication_update_request'] is None):
            raise ValueError("Missing the required parameter `replication_update_request` when calling `patch_replication_by_id`")  # noqa: E501

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replicationID'] = local_var_params['replication_id']  # noqa: E501

        query_params = []
        if 'validate' in local_var_params:
            query_params.append(('validate', local_var_params['validate']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        if 'replication_update_request' in local_var_params:
            body_params = local_var_params['replication_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_replication(self, replication_creation_request, **kwargs):  # noqa: E501,D401,D403
        """Register a new replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_replication(replication_creation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReplicationCreationRequest replication_creation_request: (required)
        :param str zap_trace_span: OpenTracing span context
        :param bool validate: If true, validate the replication, but don't save it.
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_replication_with_http_info(replication_creation_request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_replication_with_http_info(replication_creation_request, **kwargs)  # noqa: E501
            return data

    def post_replication_with_http_info(self, replication_creation_request, **kwargs):  # noqa: E501,D401,D403
        """Register a new replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_replication_with_http_info(replication_creation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReplicationCreationRequest replication_creation_request: (required)
        :param str zap_trace_span: OpenTracing span context
        :param bool validate: If true, validate the replication, but don't save it.
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_replication_prepare(replication_creation_request, **kwargs)

        return self.api_client.call_api(
            '/api/v2/replications', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replication',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_replication_async(self, replication_creation_request, **kwargs):  # noqa: E501,D401,D403
        """Register a new replication.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param ReplicationCreationRequest replication_creation_request: (required)
        :param str zap_trace_span: OpenTracing span context
        :param bool validate: If true, validate the replication, but don't save it.
        :return: Replication
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_replication_prepare(replication_creation_request, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/replications', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type='Replication',  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_replication_prepare(self, replication_creation_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['replication_creation_request', 'zap_trace_span', 'validate']  # noqa: E501
        self._check_operation_params('post_replication', all_params, local_var_params)
        # verify the required parameter 'replication_creation_request' is set
        if ('replication_creation_request' not in local_var_params or
                local_var_params['replication_creation_request'] is None):
            raise ValueError("Missing the required parameter `replication_creation_request` when calling `post_replication`")  # noqa: E501

        path_params = {}

        query_params = []
        if 'validate' in local_var_params:
            query_params.append(('validate', local_var_params['validate']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        if 'replication_creation_request' in local_var_params:
            body_params = local_var_params['replication_creation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params

    def post_validate_replication_by_id(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Validate a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_validate_replication_by_id(replication_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_validate_replication_by_id_with_http_info(replication_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_validate_replication_by_id_with_http_info(replication_id, **kwargs)  # noqa: E501
            return data

    def post_validate_replication_by_id_with_http_info(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Validate a replication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_validate_replication_by_id_with_http_info(replication_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_validate_replication_by_id_prepare(replication_id, **kwargs)

        return self.api_client.call_api(
            '/api/v2/replications/{replicationID}/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_validate_replication_by_id_async(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        """Validate a replication.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str replication_id: (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_validate_replication_by_id_prepare(replication_id, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/replications/{replicationID}/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_validate_replication_by_id_prepare(self, replication_id, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['replication_id', 'zap_trace_span']  # noqa: E501
        self._check_operation_params('post_validate_replication_by_id', all_params, local_var_params)
        # verify the required parameter 'replication_id' is set
        if ('replication_id' not in local_var_params or
                local_var_params['replication_id'] is None):
            raise ValueError("Missing the required parameter `replication_id` when calling `post_validate_replication_by_id`")  # noqa: E501

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replicationID'] = local_var_params['replication_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
