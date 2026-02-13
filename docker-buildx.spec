%undefine _debugsource_packages

Name:		docker-buildx
Version:	0.31.1
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
#VERSION=%{version} REVISION=%{release} hack/build
export CGO_ENABLED=1
go build -mod=vendor -buildmode=pie -ldflags "-X github.com/docker/buildx/version.Version=%{version} -X github.com/docker/buildx/version.Revision=%{release}" -o docker-buildx ./cmd/buildx

%install
install -d -m 0755 %{buildroot}/%{_libexecdir}/docker/cli-plugins
install -p -m 0755 docker-buildx %{buildroot}/%{_libexecdir}/docker/cli-plugins/

%files
%dir %{_libexecdir}/docker
%dir %{_libexecdir}/docker/cli-plugins
%{_libexecdir}/docker/cli-plugins/*
