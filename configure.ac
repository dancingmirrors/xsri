dnl Process this file with autoconf to produce a configure script.

AC_INIT
AC_CONFIG_SRCDIR([xsri.c])

dnl $Format: "AM_INIT_AUTOMAKE(xsri, $ReleaseVersion$)" $
AM_INIT_AUTOMAKE(xsri, 2.1.0)

dnl Specify a configuration file
AM_CONFIG_HEADER(config.h)

dnl Initialize maintainer mode
AM_MAINTAINER_MODE

AC_PROG_CC
AM_PROG_CC_STDC
AC_PROG_INSTALL

changequote(,)dnl
if test "x$GCC" = "xyes"; then
  case " $CFLAGS " in
  *[\ \	]-Wall[\ \	]*) ;;
  *) CFLAGS="$CFLAGS -Wall -Wno-deprecated-declarations" ;;
  esac
fi
changequote([,])dnl

dnl library checks (not using macros/ directory)

PKG_CHECK_MODULES(GTK, x11 gtk+-2.0 >= 1.3.13 gdk-pixbuf-2.0,,
    AC_MSG_ERROR([*** GTK+-2.0 must be installed to compile xsri]))

AC_CHECK_LIB(m, sqrt)

AC_SUBST(GTK_CFLAGS)
AC_SUBST(GTK_LIBS)

adnl Output the Makefiles

AC_CONFIG_FILES([
Makefile
xsri.spec
])
AC_OUTPUT
