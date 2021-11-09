io
==

.. code-block:: go

   type Reader interface {
       Read(p []byte) (n int, err error)
   }

   type Writer interface {
       Write(p []byte) (n int, err error)
   }

   // 多了偏移量
   type ReaderAt interface {
       ReadAt(p []byte, off int64) (n int, err error)
   }

   type WriterAt interface {
       WriteAt(p []byte, off int64) (n int, err error)
   }

   type ReaderFrom interface {
       ReadFrom(r Reader) (n int64, err error)
   }

   type WriterTo interface {
       WriteTo(w Writer) (n int64, err error)
   }

   type Seeker interface {
       Seek(offset int64, whence int) (ret int64, err error)
   }

   type Closer interface {
       Close() error
   }

实现了 io.Reader 接口或 io.Writer 接口的类型

- os.File 同时实现了 io.Reader 和 io.Writer
- strings.Reader 实现了 io.Reader
- bufio.Reader/Writer 分别实现了 io.Reader 和 io.Writer
- bytes.Buffer 同时实现了 io.Reader 和 io.Writer
- bytes.Reader 实现了 io.Reader
- compress/gzip.Reader/Writer 分别实现了 io.Reader 和 io.Writer
- crypto/cipher.StreamReader/StreamWriter 分别实现了 io.Reader 和 io.Writer
- crypto/tls.Conn 同时实现了 io.Reader 和 io.Writer
- encoding/csv.Reader/Writer 分别实现了 io.Reader 和 io.Writer
- mime/multipart.Part 实现了 io.Reader
- net/conn 分别实现了 io.Reader 和 io.Writer(Conn接口定义了Read/Write)

文件读取
--------

#. 读取小文件

   .. code-block:: go

      func ReadAll(filePath string) ([]byte, error) {

         // f 是 os.File
         f, err := os.Open(filePath)
         if err != nil {
            return nil, err
         }
         return ioutil.ReadAll(f)
      }


   或者使用 ioutil

   .. code-block:: go

      data, err := ioutil.ReadAll(filename)

#. 逐行读取

   .. code-block:: go

      func ReadLines(filePath string) error {
      	f, err := os.Open(filePath)
      	if err != nil {
      		fmt.Println(err.Error())
      		return err
      	}

      	defer f.Close()

      	reader := bufio.NewReader(f)
      	for {
      		line, err := reader.ReadBytes('\n')
      		fmt.Print(string(line))
      		if err != nil {
      			if err == io.EOF {
      				return nil
      			}
      			return err
      		}
      	}
      }