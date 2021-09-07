# Pull Request 초기 설정



### Fork

##### 1.  [강민수의 github](https://github.com/Mingdoo/coding_test_boom)으로 들어가서 우측 상단에 있는 Fork버튼을 누른다.

![image-20210907215207587](PR tutorial.assets/image-20210907215207587.png)

##### 2. 본인의 github계정에 들어가 repository에 `coding_test_boom`이 생성되었는지 확인한다.

![image-20210907215301585](PR tutorial.assets/image-20210907215301585.png)

##### 3. 본인의 로컬 저장소로 `coding_test_boom`을 clone을 뜬다.

```bash
git clone <https://github.com/<계정id>/coding_test_boom.git
```



### PR

##### 0. 로컬 저장소에서 pull을 당긴다.

```bash
git pull origin master
```



##### 1. 본인의 계정 repo에 자신이 작성한 코드를 담아 push한다.

```bash
git add .
git commit -m '<commit message>'
git push origin master
```



##### 2. 본인 계정으로 github에 로그인 한 뒤 본인 계정의 `coding_test_boom` repo로 들어가 좌측 상단의 Pull requests를 클릭한다.



![image-20210907215746146](PR tutorial.assets/image-20210907215746146.png)



##### 3. 우상단의 New pull request를 클릭한다.

![image-20210907215839763](PR tutorial.assets/image-20210907215839763.png)



##### 4. Create pull request를 클릭한 후 간단한 메세지와 함께 merge를 요청한다.

