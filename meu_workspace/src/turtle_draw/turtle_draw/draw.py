import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill
from geometry_msgs.msg import Twist
import time

class TurtleDraw(Node):
    def __init__(self):
        super().__init__('turtle_draw')
        self.spawn_client = self.create_client(Spawn, 'spawn')
        self.kill_client = self.create_client(Kill, 'kill')
        self.velocity_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def draw_shape(self):
        # Esperar pelos serviços
        self.get_logger().info("Waiting for services...")
        self.spawn_client.wait_for_service()
        self.kill_client.wait_for_service()

        # Spawn a new turtle
        spawn_request = Spawn.Request()
        spawn_request.x = 5.5
        spawn_request.y = 5.5
        spawn_request.theta = 0.0  # Corrigido para ser float
        spawn_request.name = 'drawer'
        future = self.spawn_client.call_async(spawn_request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info(f'Successfully spawned {future.result().name}')
        else:
            self.get_logger().error('Failed to spawn turtle')
            return

        # Move in a square
        twist = Twist()
        for _ in range(4):
            # Move forward
            twist.linear.x = 2.0
            twist.angular.z = 0.0
            self.velocity_publisher.publish(twist)
            time.sleep(1)

            # Rotate in place
            twist.linear.x = 0.0
            twist.angular.z = 1.57  # About 90 degrees in radians
            self.velocity_publisher.publish(twist)
            time.sleep(1)

        # Stop the turtle
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.velocity_publisher.publish(twist)

        # Kill the spawned turtle
        kill_request = Kill.Request()
        kill_request.name = 'drawer'
        self.kill_client.call_async(kill_request)
        self.get_logger().info('Finished drawing and killed the turtle.')

def main(args=None):
    rclpy.init(args=args)
    turtle_draw = TurtleDraw()
    turtle_draw.draw_shape()
    rclpy.spin(turtle_draw)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
