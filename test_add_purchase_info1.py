import pandas as pd
import pandas.testing
import pytest
from PyQt5 import QtWidgets
from Main import Main_Function


def input_test_data(window, detect_class, detect_quality_count):
    # 分三次加入购买信息表
    window.camera.detect_class = detect_class
    window.camera.detect_count = detect_quality_count
    window.add_purchase_info()
    return window.purchase_info


def test_01():
    app = QtWidgets.QApplication([])
    window = Main_Function()

    # 模拟摄像头获得的水果信息, 对应下面的3次操作
    detect_class_list, detect_quality_count = [0, 5, 0], [[1, 0], [1, 0], [2, 1]]
    # 初始化表格信息
    info_head = ['水果名称', '新鲜程度（优/劣）', '单价', '单位', '重量', '数量', '折扣', '总价']
    info_dtypes = [str, str, float, str, float, int, float, float]
    purchase_result1 = pd.DataFrame({info_head[i]: [0] for i in range(len(info_head))})
    for i in range(len(info_head)):
        purchase_result1[info_head[i]] = purchase_result1[info_head[i]].astype(info_dtypes[i])

    # 1. 购买清单加入了1个优质苹果
    example1 = ['苹果', '1优，0劣', 3.75, '元/个', 0.0, 1, -0.375, 3.375]
    purchase_result1.loc[0] = pd.Series({info_head[i]: example1[i] for i in range(len(info_head))})
    # 2. 购买清单加入了1个优质石榴
    example2 = ['石榴', '1优，0劣', 5.0, '元/个', 0.0, 1, -0.0, 5.0]
    row2 = pd.Series({info_head[i]: example2[i] for i in range(len(info_head))})
    purchase_result2 = pd.concat([purchase_result1.copy(), row2.to_frame().T]).reset_index(drop=True)
    # 3. 购买清单又加入了2个优质苹果，1个劣质苹果
    example3 = ['苹果', '3优，1劣', 3.75, '元/个', 0.0, 4, -1.5, 13.5]
    updated_row1 = pd.Series({info_head[i]: example3[i] for i in range(len(info_head))})
    purchase_result3 = pd.concat([updated_row1.to_frame().T,
                                  pd.DataFrame([purchase_result2.iloc[1]])]).reset_index(drop=True)

    # 三次操作后，分别达到的预期结果
    expected = [purchase_result1, purchase_result2, purchase_result3]
    for i in range(3):
        purchase_info = input_test_data(window, detect_class_list[i], detect_quality_count[i])
        assert purchase_info.equals(expected[i])
        print(f'\n测试路径{i+1}通过', end='')


if __name__ == "__main__":
    pytest.main()
