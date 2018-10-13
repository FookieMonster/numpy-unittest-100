# numpy-unittest-100
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)

ユニットテストフレームワークを利用したNumPyの練習問題100

![screenshot](https://user-images.githubusercontent.com/7298626/46901704-35376e00-cef3-11e8-81de-039408699990.png)

## 説明
NumPy公式チュートリアルのトピック毎にテストケースのクラスがあります。  
そして、機能毎にテストメソッドがあるので、その実行結果をAssert文を書いて当てる演習問題です。

## 動作環境
* Python 3
* NumPy
* PyCharm (推奨)

## テストケース
| テストケース | トピック |
----|---- 
| test_array_basic.py | NumPyの基礎 |
| test_array_broadcast.py | ブロードキャスト |
| test_array_creation.py | 配列の生成 |
| test_array_eye.py | 単位行列 |
| test_array_operation.py | 基本的な操作 |
| test_array_reshape.py | 形状の操作 |
| test_array_select.py | 配列の選択 |
| test_array_slicing.py | インデックス参照とスライス |
| test_array_stack.py | 配列のスタック |
| test_array_stats.py | 統計関数 |
| test_array_ufunc.py | ユニバーサル関数 |

## 使い方
1. このリポジトリをクローン
1. PyCharm(推奨)でプロジェクトを作成し開く
1. クローン直後は間違ったAssert文になっているので全テストが失敗します
1. NumPy公式チュートリアルを参考にして正しいAssert文に修正して下さい
1. 全問正解すると上記のスクショのような「All tests passed」のグリーンバーになります

## サンプル
（問題１）　xの部分のコードを書いて正しいAssert文にして下さい。
~~~
import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayEye(unittest.TestCase):

    def test_eye_NxN(self):
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

    def test_eye_NxM(self):
        metrix = np.eye(2, 3)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x]]))
    
    def test_eye_k1(self):
        metrix = np.eye(3, k=1)
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

if __name__ == '__main__':
    unittest.main()
~~~

## 関連Webサイト
* [NumPyの演習問題100 (numpy-unittest-100)](https://note.mu/fookiemonster/n/n17276af88b7f)
* [NumPy公式チュートリアルを効率的に学習する方法](https://note.mu/fookiemonster/n/n7ce86785271f)

## ライセンス
[MITライセンス](https://github.com/tcnksm/tool/blob/master/LICENCE)

## 参考文献
* NumPy - [Quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
* Python - [Unittest](https://docs.python.jp/3/library/unittest.html)
* Rougier - [100 numpy exercises](https://github.com/rougier/numpy-100)
* 東京大学 松尾研究室 - [Numpy Test System](https://weblab.t.u-tokyo.ac.jp/)
