![screenshot](https://user-images.githubusercontent.com/7298626/46781172-52393900-cd5b-11e8-8c5e-c9689cf30027.png)

# numpy-unittest-100
ユニットテストフレームワークを利用したNumPyの演習問題100

[Webサイト](https://note.mu/fookiemonster/n/n7ce86785271f)

## 説明 

## 動作環境
* Python 3系
* PyCharm (推奨)

## ファイル構成
| テストケース | トピック |
----|---- 
| test_array_basic.py | NumPyの基礎 |
| test_array_broadcast.py | ブロードキャスト |
| test_array_creation.py | 配列の生成 |
| test_array_eye.py | 単位行列 |
| test_array_operation.py | 基本的な操作 |
| test_array_reshape.py | 形状の操作 |
| test_array_select.py | 検索 |
| test_array_slicing.py | スライス |
| test_array_stack.py | スタック |
| test_array_stats.py | 統計 |
| test_array_ufunc.py | ユニバーサル関数 |

## サンプル
~~~
import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayEye(unittest.TestCase):

    def test_eye_NxN(self):
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[1, 0, 0],
                                             [0, 1, 0],
                                             [0, 0, 1]]))

    def test_eye_NxM(self):
        metrix = np.eye(2, 3)
        assert_array_equal(metrix, np.array([[1, 0, 0],
                                             [0, 1, 0]]))

if __name__ == '__main__':
    unittest.main()
~~~

## ライセンス
[MITライセンス](https://github.com/tcnksm/tool/blob/master/LICENCE)

### 参考文献
* Rougier - 100 numpy exercises.
* 東大松尾研 - Numpy Test System.
