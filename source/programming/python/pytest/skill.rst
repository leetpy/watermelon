技巧
====

#. 类全局共享

   有时候在 Test 类中需要用到共同的变量，直接写到构造函数或 class
   是无法共享的，我们需要借助其它方式：

   .. code-block:: python

      @pytest.fixture(name="sample_manager", scope="class")
      def sample_manager_fixture():
          class SampleManager:
              def __init__(self):
                  self.last_value = 0

          return SampleManager()


      class TestSample:
          testcases = [("name1", 1), ("name2", 2), ("name3", 3), ("name4", 4)]

          def test_order(self, sample_manager):
              print(sample_manager.last_value)

          @pytest.mark.parametrize(('testname', 'testInput'), testcases)
          def test_run(self, testname, testInput, sample_manager):
              if sample_manager.last_value >= 10:
                  sample_manager.last_value += random.randint(1, 10)
              else:
                  sample_manager.last_value += 5

              print(sample_manager.last_value)