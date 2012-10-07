Date: 2012-10-06
Title: Archive, compress, unpack and uncompress files using tar, star, gzip, and bzip2
Objective: 06
Category: a. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA

tar
===

Create a tar file from a folder called test1:

    :::bash
    $ tar cvf test1.tar test1

* c = create
* v = verbose
* f = file

Extract test1.tar

    :::bash
    $ tar xvf test1.tar</code>
* x = extract
* v = verbose
* f = file

List contents of tar archive

    :::bash
    $ tar tf test1.tar</code>

star
====

Man page for star: [star](http://linux.die.net/man/1/star)

gzip
====

This is most commonly used in combination with tar, using the z switch. Tar itself does not compress, it just packs. 

    :::bash
    $ tar cvzf test1.tar.gz test1</code>

Although it can be used by itself

    :::bash
    $ gzip test1</code>

 <code>gunzip test1.gz</code>
# note that this does not preserve the .gz file, it extracts it and removes it. 

bzip2
=====

bzip2 uses a different algorithm to compress files than the other tools, but very similar options

Create a bzip2 file

    :::bash
    $ bzip2 test1</code>
    # note that this does not preserve the original file(s),
    # it will compress and delete the uncompressed version
    # also does not compress directories, only files. 

Check out the man page: [bzip2](http://bzip.org/1.0.5/bzip2.txt)