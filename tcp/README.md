## In one CLI terminal:

```bash
python server.py
```

## In another CLI terminal running at the same time:

(Maybe in a VM host on the same computer that the server is running on.)

```bash
python client.py
```

Then you should see this message get printed to the client CLI:

```bash
you connected to the server
```

And in the CLI terminal for your server, you should see this message get printed:

```bash
received connection from ('some-host-name.local', 8000)
```
