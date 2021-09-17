import os
import oss
import mysql


def clear_oss_files(debug: bool, dirname: str):
    """
    批量删除云存储中某一个文件夹下的所有文件
    :param debug: 是否执行此操作
    :param dirname: 文件夹的名称

    用法 ::

        >>> import debug
        >>> debug.clear_oss_files(
                debug=True,
                dirname='bottles/'
            )

    """
    if debug:
        bucket = oss.BUCKET
        bucket.delete_files(dirname=dirname)


def clear_mysql_table(debug: bool, table: str):
    """
    清空云数据库中的某一个数据表
    :param debug: 是否执行此操作
    :param table: 数据表的名称

    用法 ::

        >>> import debug
        >>> debug.clear_mysql_table(
                debug=True,
                table='bottles'
            )

    """
    if debug:
        db = mysql.DATABASE
        db.clear_table(table=table)


if __name__ == '__main__':
    DEBUG = True if os.getenv('DEBUG') == 'True' else False

    # 批量删除云存储中`bottles`文件夹下的所有文件
    clear_oss_files(
        debug=DEBUG,
        dirname='bottles/'
    )
    # 清空云数据库中的数据表
    clear_mysql_table(
        debug=DEBUG,
        table='users'
    )
    clear_mysql_table(
        debug=DEBUG,
        table='bottles'
    )
