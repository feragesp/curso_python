# FROM: Imagen de base
FROM node:24.4.0-alpine3.22

RUN addgroup react && adduser -S -G react react
USER react

# COPIAR FICHEROS AL SERVER
WORKDIR /app/
COPY --chown=react package*.json .

RUN npm install

COPY --chown=react . .

ENV API=https://apiv1.miweb.com
EXPOSE 5173

CMD ["npm", "run", "dev"]