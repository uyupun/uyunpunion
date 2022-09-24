syntax enable           " シンタックスハイライトを有効

set fenc=utf-8          " 文字エンコードをUTF-8に設定
set nobackup            " バックアップファイルを作成しない
set noswapfile          " スワップファイルを作成しない
set autoread            " Vim以外で変更された内容を自動で反映する

set showcmd             " 入力中のコマンドをステータスに表示
set number              " 行番号の表示
set ruler               " カーソルの位置表示
set cursorline          " カーソル行の背景色を変更
set cursorcolumn        " カーソル位置のカラムの背景色を変更
set virtualedit=onemore " 行末の１文字先まで移動できるようにする
set cindent             " 自動インデント
set showmatch           " 対応する括弧を強調表示
set visualbell          " ビープ音を可視化
set belloff=all         " ビープ音をOFF
set laststatus=2        " ステータスラインを常に表示
set mouse=a             " マウスを有効にする

" インデントを半角スペースとして扱うための設定
set expandtab
set tabstop=2
set shiftwidth=2
