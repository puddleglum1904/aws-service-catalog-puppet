from unittest import skip
from servicecatalog_puppet.workflow import tasks_unit_tests_helper


class AssertionBaseTaskTest(tasks_unit_tests_helper.PuppetTaskUnitTest):
    manifest_file_path = "manifest_file_path"

    def setUp(self) -> None:
        from servicecatalog_puppet.workflow.assertions import assertion_base_task

        self.module = assertion_base_task

        self.sut = self.module.AssertionBaseTask(
            manifest_file_path=self.manifest_file_path
        )

        self.wire_up_mocks()
