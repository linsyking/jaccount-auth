# Python Jaccount Auth 

A small plugin to help use jaccount login in python programs.

Forked from tc-imba's [python-jaccount-cli](https://github.com/tc-imba/python-jaccount-cli).

## Example

```python
import asyncio
from getpass import getpass

from jaccount_cli import JaccountCLIAsyncIO


async def main():
    async with JaccountCLIAsyncIO("https://umjicanvas.com/login/openid_connect") as cli:
        await cli.init()

        captcha_ascii = cli.captcha_generate_ascii()
        print()
        print(captcha_ascii)
        print()
        # or you can use
        # cli.captcha_show_external()

        captcha = input("Please enter the shown captcha: ")
        username = input("Please enter jaccount username: ")
        password = getpass("Please enter password: ")

        await cli.login(username, password, captcha)

        async with cli.session.get(
            "https://umjicanvas.com/api/v1/users/self/favorites/courses?include[]=term&exclude[]=enrollments",
            headers={"Accept": "application/json"},
        ) as response:
            print(await response.text())

        # print cookies
        cookies = cli.get_cookies()
        for key, cookie in cookies.items():
            print('Key: "%s", Value: "%s"' % (cookie.key, cookie.value))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
```

## License

MIT
