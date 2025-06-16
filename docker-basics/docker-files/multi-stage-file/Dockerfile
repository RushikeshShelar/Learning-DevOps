# Single-stage Dockerfile for a Spring Boot application (878MB)

# FROM eclipse-temurin:21.0.2_13-jdk-jammy
# WORKDIR /app
# COPY .mvn/ .mvn
# COPY mvnw pom.xml ./
# RUN ./mvnw dependency:go-offline
# COPY src ./src
# CMD ["./mvnw", "spring-boot:run"]

# Multi-stage Dockerfile for a Spring Boot application (434MB)
# FROM eclipse-temurin:21.0.2_13-jdk-jammy AS builder
# WORKDIR /opt/app
# COPY .mvn/ .mvn
# COPY mvnw pom.xml ./
# RUN ./mvnw dependency:go-offline
# COPY src ./src
# RUN ./mvnw clean install 

# FROM eclipse-temurin:21.0.2_13-jre-jammy AS final
# WORKDIR /opt/app
# EXPOSE 8080
# COPY --from=builder /opt/app/target/*.jar /opt/app/*.jar
# ENTRYPOINT ["java", "-jar", "/opt/app/*.jar"]