输出颜色
========

.. code-block:: bash

    RED='\033[31m'
    GREEN='\033[32m'
    BLUE='\033[36m'
    NC='\033[0m'

    # 需要加 -e 参数
    echo -e "${RED}hello world!${NC}"
