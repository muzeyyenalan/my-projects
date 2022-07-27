FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 5080

ENV ASPNETCORE_URLS=http://+:5080
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Example.csproj", "./"]
RUN dotnet restore "Example.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Example.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Example.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Example.dll"]