
def b64encode(bytes_data:bytes)->str:
    #base64用のencode変換テーブル
    table ={bin(j)[2:].rjust(6,"0") : k for j,k in enumerate([chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]+list(map(str,range(0,10)))+["+","/"])}
    return (out:=str().join(map(lambda x:table[x],(lambda list_,chunk:(list_[i:i+chunk] for i in range(0,chunk*(len(list_)//chunk)if len(list_)%chunk==0 else chunk*(len(list_)//chunk) + 1,chunk)))((out:=str().join(list(map(lambda x: bin(x)[2:].rjust(8,"0"),bytes.fromhex(bytes_data.hex())))))+(6-len(out)%6)%6*"0",6))))+(4-len(out)%4)%4*"="
def b64decode(b64_text:str)->bytes:
    #base64用のdecode変換テーブル
    table ={k:bin(j)[2:].rjust(6,"0") for j,k in enumerate([chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]+list(map(str,range(0,10)))+["+","/"])}
    return bytes(map(lambda x:int(x,base=2),filter(lambda x:len(x)==8,(lambda list_,chunk:(list_[i:i+chunk] for i in range(0,chunk*(len(list_)//chunk) if len(list_)%chunk==0 else chunk*(len(list_)//chunk)+1,chunk)))(str().join(("" if i=="=" else table[i] for i in b64_text)),8))))

if __name__=="__main__":
    #テスト
    import base64
    t="こんにちはhello".encode("utf-8")
    assert base64.b64encode(t)==bytes(b64encode(t).encode())

    print(b64encode(t))
    print(
        b64decode(b64encode(t)).decode("utf-8")
    )