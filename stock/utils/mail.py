from typing import List

import yagmail


class Mail:

    def sendMail(self, msg: str, title: str, receivers: List[str]) -> None:

        yag = yagmail.SMTP(
            host="smtp.qq.com", user="1296915319@qq.com", password="satbjxbqwtaqhjcd",
            smtp_ssl=True)
        try:
            yag.send(receivers, title, msg)
        except Exception as e:
            print(e)
        finally:
            yag.close()


def main():
    mail = Mail()
    mail.sendMail("hello", "hello", ["1296915319@qq.com"])


if __name__ == "__main__":
    main()
