# s2p-converter

## summary(JPN:概要)


 JPN:NanoVNAで作成した順方向s2pフィアル（S11,S21のみ）逆方向s2pファイル(S11,S21のみ）を入力して、S11,S21,S12,S22がそろったs2pファイルを出力します。


## usage (JPN:使い方）

On Linux Shell,

> python3 convert.py file1.s2p file2.s2p >file3.s2p

|item | i/o | description |
----|----|----
|convert.py |- | Python program|
|file1.s2p | input| NanoVNA output s2p format file(JPN:NanoVNA出力のs2p形式ファイル 順方向接続)|
|file2.s2p| input| NanoVNA output s2p format file(JPN:NanoVNA出力のs2p形式ファイル 逆方向接続)|
|file3.s2p | output| converted s2p format file(JPN:合成したs2p形式ファイル)|


## Tested(JPN:テストした環境)

|Environment|Version|
---|---|
|OS| 20.04.1 LTS (Focal Fossa)|
|Language|Python 3.8.5|
