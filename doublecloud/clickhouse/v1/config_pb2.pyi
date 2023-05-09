from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickhouseConfig(_message.Message):
    __slots__ = ["log_level", "max_connections", "max_concurrent_queries", "keep_alive_timeout", "uncompressed_cache_size", "mark_cache_size", "max_table_size_to_drop", "max_partition_size_to_drop", "timezone", "background_pool_size", "background_schedule_pool_size", "background_fetches_pool_size", "background_move_pool_size", "background_common_pool_size", "background_merges_mutations_concurrency_ratio", "total_memory_profiler_step", "total_memory_tracker_sample_probability", "merge_tree", "compression", "graphite_rollup", "kafka", "kafka_topics", "rabbitmq"]
    class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        LOG_LEVEL_INVALID: _ClassVar[ClickhouseConfig.LogLevel]
        LOG_LEVEL_TRACE: _ClassVar[ClickhouseConfig.LogLevel]
        LOG_LEVEL_DEBUG: _ClassVar[ClickhouseConfig.LogLevel]
        LOG_LEVEL_INFORMATION: _ClassVar[ClickhouseConfig.LogLevel]
        LOG_LEVEL_WARNING: _ClassVar[ClickhouseConfig.LogLevel]
        LOG_LEVEL_ERROR: _ClassVar[ClickhouseConfig.LogLevel]
    LOG_LEVEL_INVALID: ClickhouseConfig.LogLevel
    LOG_LEVEL_TRACE: ClickhouseConfig.LogLevel
    LOG_LEVEL_DEBUG: ClickhouseConfig.LogLevel
    LOG_LEVEL_INFORMATION: ClickhouseConfig.LogLevel
    LOG_LEVEL_WARNING: ClickhouseConfig.LogLevel
    LOG_LEVEL_ERROR: ClickhouseConfig.LogLevel
    class MergeTree(_message.Message):
        __slots__ = ["replicated_deduplication_window", "replicated_deduplication_window_seconds", "parts_to_delay_insert", "parts_to_throw_insert", "inactive_parts_to_delay_insert", "inactive_parts_to_throw_insert", "max_replicated_merges_in_queue", "number_of_free_entries_in_pool_to_lower_max_size_of_merge", "max_bytes_to_merge_at_min_space_in_pool", "max_bytes_to_merge_at_max_space_in_pool", "min_bytes_for_wide_part", "min_rows_for_wide_part", "ttl_only_drop_parts", "merge_with_ttl_timeout", "merge_with_recompression_ttl_timeout", "allow_remote_fs_zero_copy_replication"]
        REPLICATED_DEDUPLICATION_WINDOW_FIELD_NUMBER: _ClassVar[int]
        REPLICATED_DEDUPLICATION_WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
        PARTS_TO_DELAY_INSERT_FIELD_NUMBER: _ClassVar[int]
        PARTS_TO_THROW_INSERT_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_PARTS_TO_DELAY_INSERT_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_PARTS_TO_THROW_INSERT_FIELD_NUMBER: _ClassVar[int]
        MAX_REPLICATED_MERGES_IN_QUEUE_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_FREE_ENTRIES_IN_POOL_TO_LOWER_MAX_SIZE_OF_MERGE_FIELD_NUMBER: _ClassVar[int]
        MAX_BYTES_TO_MERGE_AT_MIN_SPACE_IN_POOL_FIELD_NUMBER: _ClassVar[int]
        MAX_BYTES_TO_MERGE_AT_MAX_SPACE_IN_POOL_FIELD_NUMBER: _ClassVar[int]
        MIN_BYTES_FOR_WIDE_PART_FIELD_NUMBER: _ClassVar[int]
        MIN_ROWS_FOR_WIDE_PART_FIELD_NUMBER: _ClassVar[int]
        TTL_ONLY_DROP_PARTS_FIELD_NUMBER: _ClassVar[int]
        MERGE_WITH_TTL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        MERGE_WITH_RECOMPRESSION_TTL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        ALLOW_REMOTE_FS_ZERO_COPY_REPLICATION_FIELD_NUMBER: _ClassVar[int]
        replicated_deduplication_window: _wrappers_pb2.Int64Value
        replicated_deduplication_window_seconds: _duration_pb2.Duration
        parts_to_delay_insert: _wrappers_pb2.Int64Value
        parts_to_throw_insert: _wrappers_pb2.Int64Value
        inactive_parts_to_delay_insert: _wrappers_pb2.Int64Value
        inactive_parts_to_throw_insert: _wrappers_pb2.Int64Value
        max_replicated_merges_in_queue: _wrappers_pb2.Int64Value
        number_of_free_entries_in_pool_to_lower_max_size_of_merge: _wrappers_pb2.Int64Value
        max_bytes_to_merge_at_min_space_in_pool: _wrappers_pb2.Int64Value
        max_bytes_to_merge_at_max_space_in_pool: _wrappers_pb2.Int64Value
        min_bytes_for_wide_part: _wrappers_pb2.Int64Value
        min_rows_for_wide_part: _wrappers_pb2.Int64Value
        ttl_only_drop_parts: _wrappers_pb2.BoolValue
        merge_with_ttl_timeout: _duration_pb2.Duration
        merge_with_recompression_ttl_timeout: _duration_pb2.Duration
        allow_remote_fs_zero_copy_replication: _wrappers_pb2.BoolValue
        def __init__(self, replicated_deduplication_window: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., replicated_deduplication_window_seconds: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., parts_to_delay_insert: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., parts_to_throw_insert: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., inactive_parts_to_delay_insert: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., inactive_parts_to_throw_insert: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_replicated_merges_in_queue: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., number_of_free_entries_in_pool_to_lower_max_size_of_merge: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_bytes_to_merge_at_min_space_in_pool: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_bytes_to_merge_at_max_space_in_pool: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min_bytes_for_wide_part: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min_rows_for_wide_part: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., ttl_only_drop_parts: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., merge_with_ttl_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., merge_with_recompression_ttl_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., allow_remote_fs_zero_copy_replication: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class Kafka(_message.Message):
        __slots__ = ["security_protocol", "sasl_mechanism", "sasl_username", "sasl_password", "enable_ssl_certificate_verification"]
        class SecurityProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            SECURITY_PROTOCOL_INVALID: _ClassVar[ClickhouseConfig.Kafka.SecurityProtocol]
            SECURITY_PROTOCOL_PLAINTEXT: _ClassVar[ClickhouseConfig.Kafka.SecurityProtocol]
            SECURITY_PROTOCOL_SSL: _ClassVar[ClickhouseConfig.Kafka.SecurityProtocol]
            SECURITY_PROTOCOL_SASL_PLAINTEXT: _ClassVar[ClickhouseConfig.Kafka.SecurityProtocol]
            SECURITY_PROTOCOL_SASL_SSL: _ClassVar[ClickhouseConfig.Kafka.SecurityProtocol]
        SECURITY_PROTOCOL_INVALID: ClickhouseConfig.Kafka.SecurityProtocol
        SECURITY_PROTOCOL_PLAINTEXT: ClickhouseConfig.Kafka.SecurityProtocol
        SECURITY_PROTOCOL_SSL: ClickhouseConfig.Kafka.SecurityProtocol
        SECURITY_PROTOCOL_SASL_PLAINTEXT: ClickhouseConfig.Kafka.SecurityProtocol
        SECURITY_PROTOCOL_SASL_SSL: ClickhouseConfig.Kafka.SecurityProtocol
        class SaslMechanism(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            SASL_MECHANISM_INVALID: _ClassVar[ClickhouseConfig.Kafka.SaslMechanism]
            SASL_MECHANISM_GSSAPI: _ClassVar[ClickhouseConfig.Kafka.SaslMechanism]
            SASL_MECHANISM_PLAIN: _ClassVar[ClickhouseConfig.Kafka.SaslMechanism]
            SASL_MECHANISM_SCRAM_SHA_256: _ClassVar[ClickhouseConfig.Kafka.SaslMechanism]
            SASL_MECHANISM_SCRAM_SHA_512: _ClassVar[ClickhouseConfig.Kafka.SaslMechanism]
        SASL_MECHANISM_INVALID: ClickhouseConfig.Kafka.SaslMechanism
        SASL_MECHANISM_GSSAPI: ClickhouseConfig.Kafka.SaslMechanism
        SASL_MECHANISM_PLAIN: ClickhouseConfig.Kafka.SaslMechanism
        SASL_MECHANISM_SCRAM_SHA_256: ClickhouseConfig.Kafka.SaslMechanism
        SASL_MECHANISM_SCRAM_SHA_512: ClickhouseConfig.Kafka.SaslMechanism
        SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        SASL_MECHANISM_FIELD_NUMBER: _ClassVar[int]
        SASL_USERNAME_FIELD_NUMBER: _ClassVar[int]
        SASL_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SSL_CERTIFICATE_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
        security_protocol: ClickhouseConfig.Kafka.SecurityProtocol
        sasl_mechanism: ClickhouseConfig.Kafka.SaslMechanism
        sasl_username: _wrappers_pb2.StringValue
        sasl_password: _wrappers_pb2.StringValue
        enable_ssl_certificate_verification: _wrappers_pb2.BoolValue
        def __init__(self, security_protocol: _Optional[_Union[ClickhouseConfig.Kafka.SecurityProtocol, str]] = ..., sasl_mechanism: _Optional[_Union[ClickhouseConfig.Kafka.SaslMechanism, str]] = ..., sasl_username: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sasl_password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., enable_ssl_certificate_verification: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class Rabbitmq(_message.Message):
        __slots__ = ["username", "password", "vhost"]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        VHOST_FIELD_NUMBER: _ClassVar[int]
        username: _wrappers_pb2.StringValue
        password: _wrappers_pb2.StringValue
        vhost: _wrappers_pb2.StringValue
        def __init__(self, username: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., vhost: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    class Compression(_message.Message):
        __slots__ = ["method", "min_part_size", "min_part_size_ratio", "level"]
        class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            METHOD_INVALID: _ClassVar[ClickhouseConfig.Compression.Method]
            METHOD_LZ4: _ClassVar[ClickhouseConfig.Compression.Method]
            METHOD_ZSTD: _ClassVar[ClickhouseConfig.Compression.Method]
            METHOD_LZ4HC: _ClassVar[ClickhouseConfig.Compression.Method]
        METHOD_INVALID: ClickhouseConfig.Compression.Method
        METHOD_LZ4: ClickhouseConfig.Compression.Method
        METHOD_ZSTD: ClickhouseConfig.Compression.Method
        METHOD_LZ4HC: ClickhouseConfig.Compression.Method
        METHOD_FIELD_NUMBER: _ClassVar[int]
        MIN_PART_SIZE_FIELD_NUMBER: _ClassVar[int]
        MIN_PART_SIZE_RATIO_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        method: ClickhouseConfig.Compression.Method
        min_part_size: int
        min_part_size_ratio: float
        level: _wrappers_pb2.Int64Value
        def __init__(self, method: _Optional[_Union[ClickhouseConfig.Compression.Method, str]] = ..., min_part_size: _Optional[int] = ..., min_part_size_ratio: _Optional[float] = ..., level: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
    class GraphiteRollup(_message.Message):
        __slots__ = ["patterns"]
        class Pattern(_message.Message):
            __slots__ = ["regexp", "function", "retention"]
            class Retention(_message.Message):
                __slots__ = ["age", "precision"]
                AGE_FIELD_NUMBER: _ClassVar[int]
                PRECISION_FIELD_NUMBER: _ClassVar[int]
                age: int
                precision: int
                def __init__(self, age: _Optional[int] = ..., precision: _Optional[int] = ...) -> None: ...
            REGEXP_FIELD_NUMBER: _ClassVar[int]
            FUNCTION_FIELD_NUMBER: _ClassVar[int]
            RETENTION_FIELD_NUMBER: _ClassVar[int]
            regexp: _wrappers_pb2.StringValue
            function: _wrappers_pb2.StringValue
            retention: _containers.RepeatedCompositeFieldContainer[ClickhouseConfig.GraphiteRollup.Pattern.Retention]
            def __init__(self, regexp: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., function: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., retention: _Optional[_Iterable[_Union[ClickhouseConfig.GraphiteRollup.Pattern.Retention, _Mapping]]] = ...) -> None: ...
        PATTERNS_FIELD_NUMBER: _ClassVar[int]
        patterns: _containers.RepeatedCompositeFieldContainer[ClickhouseConfig.GraphiteRollup.Pattern]
        def __init__(self, patterns: _Optional[_Iterable[_Union[ClickhouseConfig.GraphiteRollup.Pattern, _Mapping]]] = ...) -> None: ...
    class GraphiteRollupEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClickhouseConfig.GraphiteRollup
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClickhouseConfig.GraphiteRollup, _Mapping]] = ...) -> None: ...
    class KafkaTopicsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClickhouseConfig.Kafka
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClickhouseConfig.Kafka, _Mapping]] = ...) -> None: ...
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_QUERIES_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    UNCOMPRESSED_CACHE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MARK_CACHE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_TABLE_SIZE_TO_DROP_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTITION_SIZE_TO_DROP_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_SCHEDULE_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FETCHES_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MOVE_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COMMON_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MERGES_MUTATIONS_CONCURRENCY_RATIO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_PROFILER_STEP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_TRACKER_SAMPLE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    MERGE_TREE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    GRAPHITE_ROLLUP_FIELD_NUMBER: _ClassVar[int]
    KAFKA_FIELD_NUMBER: _ClassVar[int]
    KAFKA_TOPICS_FIELD_NUMBER: _ClassVar[int]
    RABBITMQ_FIELD_NUMBER: _ClassVar[int]
    log_level: ClickhouseConfig.LogLevel
    max_connections: _wrappers_pb2.Int64Value
    max_concurrent_queries: _wrappers_pb2.Int64Value
    keep_alive_timeout: _duration_pb2.Duration
    uncompressed_cache_size: _wrappers_pb2.Int64Value
    mark_cache_size: _wrappers_pb2.Int64Value
    max_table_size_to_drop: _wrappers_pb2.Int64Value
    max_partition_size_to_drop: _wrappers_pb2.Int64Value
    timezone: _wrappers_pb2.StringValue
    background_pool_size: _wrappers_pb2.Int64Value
    background_schedule_pool_size: _wrappers_pb2.Int64Value
    background_fetches_pool_size: _wrappers_pb2.Int64Value
    background_move_pool_size: _wrappers_pb2.Int64Value
    background_common_pool_size: _wrappers_pb2.Int64Value
    background_merges_mutations_concurrency_ratio: _wrappers_pb2.Int64Value
    total_memory_profiler_step: _wrappers_pb2.Int64Value
    total_memory_tracker_sample_probability: _wrappers_pb2.DoubleValue
    merge_tree: ClickhouseConfig.MergeTree
    compression: _containers.RepeatedCompositeFieldContainer[ClickhouseConfig.Compression]
    graphite_rollup: _containers.MessageMap[str, ClickhouseConfig.GraphiteRollup]
    kafka: ClickhouseConfig.Kafka
    kafka_topics: _containers.MessageMap[str, ClickhouseConfig.Kafka]
    rabbitmq: ClickhouseConfig.Rabbitmq
    def __init__(self, log_level: _Optional[_Union[ClickhouseConfig.LogLevel, str]] = ..., max_connections: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_concurrent_queries: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., keep_alive_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., uncompressed_cache_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., mark_cache_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_table_size_to_drop: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_partition_size_to_drop: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., timezone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., background_pool_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., background_schedule_pool_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., background_fetches_pool_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., background_move_pool_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., background_common_pool_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., background_merges_mutations_concurrency_ratio: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., total_memory_profiler_step: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., total_memory_tracker_sample_probability: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., merge_tree: _Optional[_Union[ClickhouseConfig.MergeTree, _Mapping]] = ..., compression: _Optional[_Iterable[_Union[ClickhouseConfig.Compression, _Mapping]]] = ..., graphite_rollup: _Optional[_Mapping[str, ClickhouseConfig.GraphiteRollup]] = ..., kafka: _Optional[_Union[ClickhouseConfig.Kafka, _Mapping]] = ..., kafka_topics: _Optional[_Mapping[str, ClickhouseConfig.Kafka]] = ..., rabbitmq: _Optional[_Union[ClickhouseConfig.Rabbitmq, _Mapping]] = ...) -> None: ...
