---
title: Angle correction for Rotators
author: Börge Mehlhorn
---
## Problem description

When using a rotation insert in a cryostat there will be two systematic errors attached to the reported rotational angle : backlash and slip.

Let us for the purpose of correcting those two errors differentiate between the measured angle $\theta_m$ and the corrected angle $\theta_c$. 

We can now propose the relation 

$$\theta_c = C_s\theta_m + C_b$$

where $C_s$ is the correction factor for the slip and $C_b$ is the correction for the backlash. Since both could be dependent on temperature and field it is important to determine those corrections at multiple point in $(T,\mu_0H)\in\mathbb{T}\times\mathbb{H}$.

## Assumptions

- The sample does not show hysteresis in the angle. 
$$\mu(\theta_c, \dot\theta_c>0)=\mu(\theta_c,\dot\theta_c<0)$$
- The slip is constant in angle.
$$\frac{\partial C_s}{\partial \theta_c} = 0$$
- Backlash occurs at each change of rotational direction.
$$C_b(\theta_c = 0) = 0 \text{ and for each point }\theta_i\text{ where } \dot\theta \text{ crosses } 0 : C_b(\theta_{i+1}) = C_b(\theta_i) + C_b$$
- After a rotation of $360^\circ$ the sample shows the same moment. (Symmetry of the rotator)
$$\mu(\theta_c) = \mu(\theta_c+2\pi)$$

## Proposed Solution

Let us assume we have data in a 2D array with columns for magnetization $\mu$ and $\theta_m$. 

This data was recorded at otherwise fixed conditions (temperature, fieldstrength, pressure).

The rotational range was greater than $360^\circ$.

1. We find the points $\theta_i$ where the direction of the rotation changes $\dot\theta=0$.
2. We split the data at those points and add $C_b$ to $\theta$ so the curves overlap perfectly. 
3. We apply a modulo operation to $\theta$.
$$\theta \to \theta\mod 2\pi$$
4. If the curves do not overlap we scale $\theta$ with $C_s$ and repeat step 3. When overlap is acieved, $C_s$ is found.

$C_b$ and $C_s$ can be set with sliders and the overlap confirmed by eye.



