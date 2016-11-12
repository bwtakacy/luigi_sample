import luigi
import luigi.cmdline
import luigi.postgres


class HelloWorldWithPGTargetTask(luigi.Task):
    task_namespace = 'examples'
    date = luigi.DateParameter()
    force = luigi.BoolParameter(significant=False, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.force is True:
            if self.output().exists():
                print('output already exists!! Will remove forcely.')
                self.remove_marker()

    def remove_marker(self):
        connection = self.output().connect()
        connection.autocommit = True

        connection.cursor().execute(
            """DELETE FROM {marker_table} WHERE update_id = '{task_id}';
            """.format(marker_table=self.output().marker_table,
                    task_id=self.task_id))

        if self.output().exists():
            print('Failed to force rerun.')
            raise ValueError()
        else:
            print('cleanup for forcely rerun done!')
            
    def output(self):
        return luigi.postgres.PostgresTarget(
            host='localhost',
            database='postgres',
            user='bwtakacy',
            password='postgres',
            table='tbl',
            update_id=self.task_id
        )

    def run(self):
        connection = self.output().connect()
        print("{task} says: Hello world on {date}!".format(task=self.__class__.__name__, date=self.date))
        self.output().touch(connection)
        connection.commit()
        connection.close()

if __name__ == '__main__':
    #luigi.run(['examples.HelloWorldTask', '--workers', '1', '--local-scheduler'])
    luigi.cmdline.luigi_run()
