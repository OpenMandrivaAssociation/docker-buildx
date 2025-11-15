%undefine _debugsource_packages

Name:		docker-buildx
Version:	0.30.0
Release:	1
Source0:	https://github.com/docker/buildx/archive/refs/tags/v%{version}.tar.gz
Summary:	Docker CLI plugin for extended build capabilities with BuildKit
URL:		https://github.com/docker/buildx
License:	Apache-2.0
Group:		Servers
BuildRequires:	golang
Requires:	docker-cli

%description
Docker CLI plugin for extended build capabilities with BuildKit

%prep
%autosetup -p1 -n buildx-%{version}

%conf

%build
VERSION=%{version} REVISION=%{release} hack/build

%install
install -d -m 0755 %{buildroot}/%{_libexecdir}/docker/cli-plugins
install -p -m 0755 bin/build/docker-buildx %{buildroot}/%{_libexecdir}/docker/cli-plugins/

%files
%dir %{_libexecdir}/docker
%dir %{_libexecdir}/docker/cli-plugins
%{_libexecdir}/docker/cli-plugins/*
