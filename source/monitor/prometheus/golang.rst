Go 使用 prometheus
==================


.. code-block:: Go

    import (
        "github.com/prometheus/client_golang/prometheus"
    )

    counter := prometheus.NewCounter(prometheus.CounterOpts{
        Name:       "rpc_durations_seconds",
		Help:       "RPC latency distributions.",
		Objectives: map[string]string{0.5: 0.05, 0.9: 0.01, 0.99: 0.001},
    })