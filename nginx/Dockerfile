FROM nginx:alpine

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create necessary directories and set permissions
RUN mkdir -p /var/log/nginx && \
    mkdir -p /var/cache/nginx && \
    mkdir -p /var/run && \
    chown -R nginx:nginx /var/log/nginx /var/cache/nginx /var/run && \
    chmod -R 755 /var/log/nginx /var/cache/nginx /var/run

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"] 