%define version 1.1.9
%define release %mkrel 1
%define name    xine-lib
%define major 1
%define build_plf 0
%define build_optimization 0

#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

%define build_pulse	1
%define build_magick	1
%define build_arts 0

%if %mdkversion < 1010
%define build_magick	0
%endif

%define build_theora 1
%if %mdkversion < 1000
%define build_theora 0
%endif

%define build_directfb 0
%define external_vcdnav 1
%define build_smb 1
%define build_alsa 1

%if %mdkversion < 920
%define build_smb 0
%endif

%if %mdkversion <= 910
%define external_vcdnav 0
%endif
%if %mdkversion <= 1010
%define external_vcdnav 0
%endif
%define build_vidix 1
%ifnarch %ix86
%define build_vidix 0
%endif

%define build_linuxfb 1

%define libname		%mklibname xine %major
%define libnamedev	%mklibname -d xine

%define bname xine
%define dvdnav 0.1.4

%define build_divx4 0
%define build_xvid 0
%define build_faad 0
%define build_win32 0
%ifarch %ix86
%define build_win32 1
%endif

%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%define build_faad 1
%endif
%{?_with_optimization: %{expand: %%global build_optimization 1}}
%{?_with_theora: %{expand: %%global build_theora 1}}
%{?_without_theora: %{expand: %%global build_theora 0}}
%{?_with_directfb: %{expand: %%global build_directfb 1}}
%{?_without_directfb: %{expand: %%global build_directfb 0}}
%{?_with_alsa: %{expand: %%global build_alsa 1}}
%{?_without_alsa: %{expand: %%global build_alsa 0}}
%{?_with_vcdnav: %{expand: %%global external_vcdnav 1}}
%{?_without_vcdnav: %{expand: %%global external_vcdnav 0}}
%{?_with_vidix: %{expand: %%global build_vidix 1}}
%{?_without_vidix: %{expand: %%global build_vidix 0}}
%{?_with_linuxfb: %{expand: %%global build_linuxfb 1}}
%{?_without_linuxfb: %{expand: %%global build_linuxfb 0}}
%{?_with_faad: %{expand: %%global build_faad 1}}
%{?_without_faad: %{expand: %%global build_faad 0}}
%{?_with_win32: %{expand: %%global build_win32 1}}
%{?_without_win32: %{expand: %%global build_win32 0}}
%{?_with_divx4: %{expand: %%global build_divx4 1}}
%{?_without_divx4: %{expand: %%global build_divx4 0}}
%{?_with_xvid: %{expand: %%global build_xvid 1}}
%{?_without_xvid: %{expand: %%global build_xvid 0}}
%{?_with_smb: %{expand: %%global build_smb 1}}
%{?_without_smb: %{expand: %%global build_smb 0}}
%{?_with_pulse: %{expand: %%global build_pulse 1}}
%{?_without_pulse: %{expand: %%global build_pulse 0}}
%{?_with_magick: %{expand: %%global build_magick 1}}
%{?_without_magick: %{expand: %%global build_magick 0}}

Name:        %{name}
Summary:     A Free Video Player (Libraries)
Version:     %{version}
Release:     %{release}
License:     GPL
Group:       System/Libraries
Source0:      http://prdownloads.sourceforge.net/xine/%name-%version.tar.bz2
URL:         http://xine.sourceforge.net
BuildRoot:   %_tmppath/%{name}-buildroot
Buildconflicts: libxine-devel < %version
Buildrequires: aalib-devel
Buildrequires: libcaca-devel >= 0.99
Buildrequires: esound-devel
Buildrequires: libvorbis-devel
Buildrequires: libspeex-devel
Buildrequires: libjack-devel
Buildrequires: libSDL-devel
Buildrequires: libmng-devel
Buildrequires: libflac-devel
Buildrequires: libgnome-vfs2-devel
BuildRequires: libmodplug-devel
BuildRequires: libgdk_pixbuf2.0-devel
%if %mdkversion >= 200710
BuildRequires: libxcb-devel
# gw this is a private dep of libxcb-devel
BuildRequires: libpthread-stubs
%endif
%if %mdkversion >= 200700
BuildRequires: libmesaglu-devel
BuildRequires: libxv-devel
BuildRequires: libxvmc-devel
BuildRequires: libxinerama-devel
%else
BuildRequires: mesaglu-devel
BuildRequires: X11-devel
%endif
%if %build_smb
BuildRequires:	libsmbclient-devel > 2.2.8a-7mdk 
%endif
%if %external_vcdnav
BuildRequires: libvcd-devel >= 0.7.19
%endif
%if %build_theora
Buildrequires: libtheora-devel
%endif
%if %build_directfb
Buildrequires: libdirectfb-devel >= 0.9.9
%endif
BuildRequires: autoconf2.5
%if %mdkversion <= 910
BuildRequires: automake1.6
%else
BuildRequires: automake1.7
%endif

%description 
xine is a free gpl-licensed video player for unix-like systems.
%if %build_plf
This package is in PLF because the AAC decoder is covered by patents.
%endif


%package -n %{bname}-plugins
Summary:     	A Free Video Player (main plugins)
Group: 		Video
Provides: %bname-xv %bname-gl %bname-oss %libname-docs %bname-speex
Provides:  %bname-dvdnav %bname-alsa %bname-musepack
Obsoletes: %bname-xv %bname-gl %bname-oss %libname-docs %bname-speex
Obsoletes: %bname-dvdnav %bname-alsa %bname-musepack
%if %build_win32
Obsoletes:	xine-plugins-win32 xine-win32
Provides:	xine-plugins-win32 xine-win32
#Suggests: win32-codecs
%endif
#gw enable this once the cdda plugin from xine-vcdx was merged too
#Provides: %bname-vcdx
#Obsoletes: %bname-vcdx
# Plugins are in versioned dir, so require the exact version
Requires:  %libname = %version

%description -n %{bname}-plugins
xine is a free gpl-licensed video player for unix-like systems.

This package includes the main plugins for xine, they allow the input
from files, Video CDs, network streams and (not encrypted) DVDs in
several video formats.  For additional plugins (support for DVDs
protected by CSS or for non free codecs) you could try the packages
from the Penguin Liberation Front home page:

http://plf.zarb.org

That page is not connected to Mandriva.
%if %build_optimization

Warning: This package was optimized for the build machine and probably won't 
run on other computers.
%endif 

%package -n %{bname}-dvdnav
Group: Video
Summary: DVD plugin for xine
#Buildrequires: libdvdnav1-devel >= %dvdnav
#Requires: libdvdnav1 >= %dvdnav
Requires: %{bname}-plugins = %version

%description -n %bname-dvdnav

xine-dvdnav provides DVD navigation support (including menus) to the
Xine media player. By default it only supports DVDs not scrambled with
CSS.


%package -n %{bname}-sdl
Group: Video
Summary: SDL video output plugin for xine
Requires: %{bname}-plugins = %version

%description -n %bname-sdl
xine is a free gpl-licensed video player for unix-like systems.

This package contains the SDL video output plugin.

%package -n %{bname}-caca
Group: Video
Summary: Caca video output plugin for xine
Requires: %{bname}-plugins = %version

%description -n %bname-caca
xine is a free gpl-licensed video player for unix-like systems.

This package contains the Caca video output plugin.


%package -n %libname
Summary:     	A Free Video Player (Libraries)
Group: 		System/Libraries
Provides:   xine-lib

%description -n %libname
xine is a free gpl-licensed video player for unix-like systems.

This package contains the shared libraries required by xine.

%package -n %libnamedev
Summary:        Devel files for xine
Group:          Development/C
Requires:	%libname = %version
Provides:	libxine-devel = %version-%release
Obsoletes: %mklibname -d xine 1

%description -n %libnamedev
xine is a free gpl-licensed video player for unix-like systems.

This package contains the development files required for compiling xine
front ends or plugins.

%if %build_arts
%package -n %{bname}-arts
Summary:        Arts plugin for xine
Group:          Video
Requires:  %{bname}-plugins = %version
Buildrequires: libarts-devel

%description -n %{bname}-arts
xine is a free gpl-licensed video player for unix-like systems.

- Arts audio output plugin
%endif

%package -n %{bname}-esd
Summary:        Esd plugin for xine
Group:          Sound
Requires:  %{bname}-plugins = %version

%description -n %{bname}-esd
xine is a free gpl-licensed video player for unix-like systems.

- Esd audio output plugin

%package -n %{bname}-jack
Summary:        Jack plugin for xine
Group:          Sound
Requires:  %{bname}-plugins = %version

%description -n %{bname}-jack
xine is a free gpl-licensed video player for unix-like systems.

- Jack audio output plugin

%if %build_pulse
%package -n %{bname}-pulse
Summary:        Pulseaudio plugin for xine
Group:          Sound
Requires:  %{bname}-plugins = %version
Provides: %bname-polyp
Obsoletes: %bname-polyp
BuildRequires: libpulseaudio-devel

%description -n %{bname}-pulse
xine is a free gpl-licensed video player for unix-like systems.

- pulseaudio audio output plugin
%endif

%if %build_magick
%package -n %{bname}-image
Summary:        ImageMagick plugin for xine
Group:          Graphics
Requires:  %{bname}-plugins = %version
BuildRequires: ImageMagick-devel > 5.5.7.15

%description -n %{bname}-image
xine is a free gpl-licensed video player for unix-like systems.

- image display plugin based on ImageMagick
%endif

%package -n %{bname}-aa
Summary:        Aalib plugin for xine
Group:          Video
Requires:  %{bname}-plugins = %version

%description -n %{bname}-aa
xine is a free gpl-licensed video player for unix-like systems.

- Aalib textmode output plugin

%package -n %{bname}-dxr3
Summary:        DXR3 plugin for xine
Group:          Video
Requires:  %{bname}-plugins = %version


%description -n %{bname}-dxr3
xine is a free gpl-licensed video player for unix-like systems.

- DXR3/Hollywood+ (MPEG2 hardware decoder) decoding/output plugin
%if %build_plf
- this version has mpeg encoding enabled using libfame
%endif

%package -n %{bname}-flac
Summary:        FLAC plugin for xine
Group:          Sound
Requires:  %{bname}-plugins = %version

%description -n %{bname}-flac
xine is a free gpl-licensed video player for unix-like systems.

- FLAC audio decoder plugin

%package -n %{bname}-gnomevfs
Summary:        GNOME VFS plugin for xine
Group:          System/Libraries
Requires:  %{bname}-plugins = %version

%description -n %{bname}-gnomevfs
xine is a free gpl-licensed video player for unix-like systems.

- GNOME VFS input plugin

%package -n %{bname}-smb
Summary:        Samba input plugin for xine
Group:          System/Libraries
Requires:  %{bname}-plugins = %version

%description -n %{bname}-smb
xine is a free gpl-licensed video player for unix-like systems.

- Samba input plugin



%if %build_divx4
%package -n %{bname}-divx4
Summary:     	Divx4 plugin for %{bname}
Group: 		Video
Requires:	%{bname}-plugins = %{version}
ExclusiveArch:	%ix86
Obsoletes:	xine-plugins-divx4
Provides:	xine-plugins-divx4
Requires:  %{bname}-plugins = %version

%description -n %{bname}-divx4
This package contains the divx4linux plugin for %{bname}. It is in
PLF because it is covered by software patents.
%endif

%if %build_faad
%package -n %{bname}-faad
Summary:     	FAAD plugin for %{bname}
Group: 	Sound
Requires:  %{bname}-plugins = %version

%description -n %{bname}-faad
This package contains the AAC decoder plugin for %{bname}. It is in
PLF because it is covered by software patents.
%endif

%if %build_xvid
%package -n %{bname}-xvid
Summary:     	XviD plugin for %{bname}
Group: 		Video
Requires:  %{bname}-plugins = %version
Obsoletes:	xine-plugins-xvid
Provides:	xine-plugins-xvid

%description -n %{bname}-xvid
This package contains the XviD plugin for %{bname}. It is in
PLF because it is covered by software patents.
%endif

%prep
%setup -q

%build

%if %mdkversion <= 1000
%define __libtoolize true
%endif

#gw for flac
export OGG_LIBS=-logg

%if !%build_optimization
export CFLAGS="%(echo %optflags|sed s/-Wp,-D_FORTIFY_SOURCE=2//)"
%configure2_5x \
%else
%{?__cputoolize: %{__cputoolize}}
#gw expanded configure2_5x macro without the CFLAGS and --build stuff
[ -f configure.in -o -f configure.ac ] && %__libtoolize --copy --force
./configure \
 	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--localstatedir=/var/lib \
	--sharedstatedir=%{_prefix}/com \
	--mandir=%{_mandir} \
	--infodir=%{_datadir}/info \
%endif
%if %external_vcdnav
  --with-external-vcdnav \
%else
  --with-internal-vcdlibs \
%endif
%if %build_directfb
  --enable-directfb \
%endif
%if ! %build_alsa
  --disable-alsa \
%endif
%if ! %build_vidix
 --disable-vidix \
%endif
%if ! %build_faad
 --disable-faad \
%endif
%if ! %build_pulse
 --disable-polypaudio \
%endif
%if ! %build_linuxfb
 --disable-fb \
%endif
 --enable-ipv6 --with-libflac
# real-codecs-path is not set so that runtime searching is used. We want
# to use either codecs from RealPlayer or real-codecs, whichever is
# present.

%make

%install

rm -rf %buildroot libxine1.lang
%makeinstall_std
%if %mdkversion >= 1020
%multiarch_binaries %buildroot%_bindir/xine-config
%endif
#clean out unpackaged files
rm -f %buildroot/%_libdir/xine/plugins/%version/*.la
rm -f %buildroot/%_libdir/xine/plugins/%version/post/*.la
rm -rf installed-docs
mv %buildroot/%_datadir/doc/xine-lib installed-docs
rm -f %buildroot/%_libdir/xine/plugins/%version/xineplug_inp_vcdo.so

%find_lang libxine1

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{bname}-plugins -f libxine1.lang
%defattr(-,root,root)
%doc installed-docs/README* installed-docs/faq.*
%_mandir/man5/xine.5*
%dir %_libdir/xine/
%dir %_libdir/xine/plugins/
%dir %_libdir/xine/plugins/%version/
%dir %_libdir/xine/plugins/%version/post/
%_libdir/xine/plugins/%version/mime.types
%if %build_alsa
%_libdir/xine/plugins/%version/xineplug_ao_out_alsa.so
%endif
%_libdir/xine/plugins/%version/xineplug_ao_out_file.so
%_libdir/xine/plugins/%version/xineplug_ao_out_none.so
%_libdir/xine/plugins/%version/xineplug_ao_out_oss.so
%_libdir/xine/plugins/%version/xineplug_inp_cdda.so
%_libdir/xine/plugins/%version/xineplug_inp_dvb.so
%_libdir/xine/plugins/%version/xineplug_inp_dvd.so
%_libdir/xine/plugins/%version/xineplug_inp_http.so
%_libdir/xine/plugins/%version/xineplug_inp_stdin_fifo.so
%_libdir/xine/plugins/%version/xineplug_inp_file.so
%_libdir/xine/plugins/%version/xineplug_inp_mms.so
%_libdir/xine/plugins/%version/xineplug_inp_net.so
%_libdir/xine/plugins/%version/xineplug_inp_pnm.so
%_libdir/xine/plugins/%version/xineplug_inp_pvr.so
%_libdir/xine/plugins/%version/xineplug_inp_rtp.so
%_libdir/xine/plugins/%version/xineplug_inp_rtsp.so
%_libdir/xine/plugins/%version/xineplug_inp_vcd.so
%_libdir/xine/plugins/%version/xineplug_inp_v4l.so
%_libdir/xine/plugins/%version/xineplug_dmx_*so
%_libdir/xine/plugins/%version/xineplug_decode_a52.so
%_libdir/xine/plugins/%version/xineplug_decode_bitplane.so
%_libdir/xine/plugins/%version/xineplug_decode_dts.so
%_libdir/xine/plugins/%version/xineplug_decode_dvaudio.so
%_libdir/xine/plugins/%version/xineplug_decode_ff.so
%_libdir/xine/plugins/%version/xineplug_decode_gdk_pixbuf.so
%_libdir/xine/plugins/%version/xineplug_decode_gsm610.so
%_libdir/xine/plugins/%version/xineplug_decode_lpcm.so
%_libdir/xine/plugins/%version/xineplug_decode_mad.so
%_libdir/xine/plugins/%version/xineplug_decode_mpc.so*
%_libdir/xine/plugins/%version/xineplug_decode_mpeg2.so
%_libdir/xine/plugins/%version/xineplug_decode_nsf.so
%_libdir/xine/plugins/%version/xineplug_decode_spu*.so
%_libdir/xine/plugins/%version/xineplug_decode_real.so
%_libdir/xine/plugins/%version/xineplug_decode_rgb.so
%_libdir/xine/plugins/%version/xineplug_decode_speex.so
%if %build_theora
%_libdir/xine/plugins/%version/xineplug_decode_theora.so
%endif
%_libdir/xine/plugins/%version/xineplug_decode_vorbis.so
%_libdir/xine/plugins/%version/xineplug_decode_yuv.so
%if %build_directfb
%_libdir/xine/plugins/%version/xineplug_vo_out_directfb.so
%endif
%if %build_linuxfb
%_libdir/xine/plugins/%version/xineplug_vo_out_fb.so
%endif
%_libdir/xine/plugins/%version/xineplug_vo_out_syncfb.so
%_libdir/xine/plugins/%version/xineplug_vo_out_opengl.so
%_libdir/xine/plugins/%version/xineplug_vo_out_none.so
%if %build_vidix
%_libdir/xine/plugins/%version/xineplug_vo_out_vidix.so
%_libdir/xine/plugins/%version/vidix/
%endif
%_libdir/xine/plugins/%version/xineplug_vo_out_xshm.so
%_libdir/xine/plugins/%version/xineplug_vo_out_xv.so
%if %mdkversion >= 200600
%_libdir/xine/plugins/%version/xineplug_vo_out_xvmc.so
%_libdir/xine/plugins/%version/xineplug_vo_out_xxmc.so
%endif
%if %mdkversion >= 200710
%_libdir/xine/plugins/%version/xineplug_vo_out_xcbshm.so
%_libdir/xine/plugins/%version/xineplug_vo_out_xcbxv.so
%endif
%if %build_win32
%_libdir/xine/plugins/%version/xineplug_decode_qt.so*
%_libdir/xine/plugins/%version/xineplug_decode_w32dll.so*
%endif
%_libdir/xine/plugins/%version/post/xineplug_post_audio_filters.so
%_libdir/xine/plugins/%version/post/xineplug_post_goom.so
%_libdir/xine/plugins/%version/post/xineplug_post_mosaico.so
%_libdir/xine/plugins/%version/post/xineplug_post_planar.so
%_libdir/xine/plugins/%version/post/xineplug_post_switch.so
%_libdir/xine/plugins/%version/post/xineplug_post_tvtime.so
%_libdir/xine/plugins/%version/post/xineplug_post_visualizations.so
%_datadir/xine

%files -n %bname-sdl
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_vo_out_sdl.so

%files -n %bname-caca
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_vo_out_caca.so

%if %build_magick
%files -n %{bname}-image
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_decode_image.so
%endif

%files -n %libname
%defattr(-,root,root)
%doc README AUTHORS TODO
%_libdir/libxine*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%doc README ChangeLog installed-docs/hackersguide
%_bindir/xine-config
%if %mdkversion >= 1020
%multiarch %multiarch_bindir/xine-config
%endif
%_mandir/man1/xine-config.1*
%_libdir/*.la
%_libdir/*.so
%_libdir/pkgconfig/libxine.pc
%_datadir/aclocal/xine.m4
%_includedir/*.h
%_includedir/xine


%if %build_arts
%files -n %{bname}-arts
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_ao_out_arts.so
%endif

%files -n %{bname}-esd
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_ao_out_esd.so

%files -n %{bname}-jack
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_ao_out_jack.so

%if %build_pulse
%files -n %{bname}-pulse
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_ao_out_pulseaudio.so
%endif

%files -n %{bname}-aa
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_vo_out_aa.so

%files -n %{bname}-flac
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_flac.so

%ifarch %{ix86} x86_64 ppc
%files -n %{bname}-dxr3
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_*dxr3*.so
%endif

%files -n %{bname}-gnomevfs
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_inp_gnome_vfs.so

%if %build_smb
%files -n %{bname}-smb
%defattr(-,root,root)
%doc README 
%_libdir/xine/plugins/%version/xineplug_inp_smb.so
%endif

%if %build_divx4
%files -n %{bname}-divx4
%defattr(-,root,root)
%_libdir/xine/plugins/%version/xineplug_decode_divx4.so*
%endif

%if %build_faad
%files -n %{bname}-faad
%defattr(-,root,root)
%_libdir/xine/plugins/%version/xineplug_decode_faad.so*
%endif

%if %build_xvid
%files -n %{bname}-xvid
%defattr(-,root,root)
%_libdir/xine/plugins/%version/xineplug_decode_xvid.so*
%endif
