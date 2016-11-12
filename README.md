# Luigi Sample Scripts

## pgtarget_with_force_rerun.py

This is a sample to create checkpoitn record in PostgreSQL table.
And this also has a forcely re-running feature.

### RUN

```
$ PYTHONPATH=. luigi --module pgtarget_with_force_rerun examples.HelloWorldWithPGTargetTask --date 2016-11-12
```

To forcely rerun

```
$ PYTHONPATH=. luigi --module pgtarget_with_force_rerun examples.HelloWorldWithPGTargetTask --date 2016-11-12 --force
```
