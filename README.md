# numpy-unittest-100
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)

ユニットテストフレームワークを利用したNumPyの練習問題100

![screenshot](https://user-images.githubusercontent.com/7298626/46901704-35376e00-cef3-11e8-81de-039408699990.png)

## 概要
NumPy公式チュートリアルの各章のトピック毎にテストケースのクラスがあります。  
各テストケースのクラス内にはNumPyの機能毎にテスト関数があります。  
その関数の実行結果を正しいAssert文を書いて当てるNumPyの演習問題です。

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
| test_array_indexing.py | インデックス参照 |
| test_array_operation.py | 基本的な操作 |
| test_array_reshape.py | 形状の操作 |
| test_array_select.py | 配列の選択 |
| test_array_slicing.py | スライス |
| test_array_stack.py | スタック |
| test_array_stats.py | 統計関数 |
| test_array_ufunc.py | ユニバーサル関数 |

## 使い方
1. このリポジトリをクローン
1. PyCharm(推奨)でプロジェクトを作成し開く
1. クローン直後は間違ったAssert文になっているので全テストが失敗します
1. NumPy公式チュートリアルを参考にして正しいAssert文に修正して下さい
1. 全問正解すると上記のスクショのような「All tests passed」のグリーンバーになります

## サンプル
以下はNumPyのインデックス参照に関する演習問題です。  
（問題１）　xの部分のコードを書いて正しいAssert文にして下さい。
~~~Python
import unittest
import numpy as np
from numpy.testing import assert_array_equal

# ファンシーなインデックス付けとトリック
class TestArrayIndexing(unittest.TestCase):

    # インデックス配列によるインデックス付け
    def test_fancy_indexing(self):
        vector = np.array([7, 6, 5])
        assert_array_equal(vector[[2, 0, 1]], np.array([x, x, x]))

    # ブール型配列によるインデックス付け
    def test_indexing_with_boolean_arrays(self):
        metrix = np.arange(9).reshape(3, 3)
        assert_array_equal(metrix > 4, np.array([[x, x, x],
                                                 [x, x, x],
                                                 [x, x, x]]))

    # ブール型配列によるインデックス付け（エレメントの選択）
    def test_indexing_with_selected_elements(self):
        metrix = np.arange(9).reshape(3, 3)
        assert_array_equal(metrix[metrix > 4], np.array([x, x, x, x]))
    
    # ブール型配列によるインデックス付け（値の代入）
    def test_indexing_with_assignments(self):
        metrix = np.arange(9).reshape(3, 3)
        metrix[metrix > 4] = 0
        assert_array_equal(metrix, np.array([[x, x, x],
                                             [x, x, x],
                                             [x, x, x]]))

if __name__ == '__main__':
    unittest.main()
~~~

## 関連Webサイト
* [NumPyの練習問題100](https://note.mu/fookiemonster/n/n17276af88b7f)
* [NumPy公式チュートリアルを効率的に学習する方法](https://note.mu/fookiemonster/n/n7ce86785271f)

## ライセンス
MITライセンス

## 参考文献
* NumPy - [Quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
* Python - [Unittest](https://docs.python.jp/3/library/unittest.html)
* Rougier - [100 numpy exercises](https://github.com/rougier/numpy-100)
* 東京大学 松尾研究室 - [Numpy Test System](https://weblab.t.u-tokyo.ac.jp/)
