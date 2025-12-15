This file is a merged representation of a subset of the codebase, containing specifically included files and files not matching ignore patterns, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: **/*
- Files matching these patterns are excluded: tmp, .idea, .venv, **/poetry.lock, **/package-lock.json, **/yarn.lock, **/__pycache__/**, **/*.pyc, **/*.pyo, **/*.iml, **/node_modules/**, **/.next/**, **/dist/**, **/.nuxt/**, **/build/**, **/.git/**, repomix.config.json, tmp
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
attack_lab/
  __init__.py
  forward_secrecy.py
  subgroup_mitm.py
  utils.py
attack_visualizer/
  static/
    script.js
    style.css
  templates/
    index.html
  app.py
  requirements.txt
benchmark_suite/
  __init__.py
  benchmark.py
  report_generator.py
  standard_params.py
crypto_engine/
  __init__.py
  elliptic_curve.py
  modular_arithmetic.py
  protocols.py
references/
  Authenticated Key Exchange Provably Secure against the MiTM Attack.md
  Measuring Small Subgroup Attacks Against Diffie-Hellman.md
  The Elliptic Curve Diffie-Hellman (ECDH).md
  The Performance of Elliptic Curve Based Group Diffie-Hellman Protocols for Secure Group Communication over Ad Hoc Networks.md
  TLS & Perfect Forward Secrecy.md
.gitignore
crypto_benchmark_report.html
Dockerfile
Implementation-Plan-Task-Lists.md
main.py
Makefile
```

# Files

## File: references/Authenticated Key Exchange Provably Secure against the MiTM Attack.md
```markdown
DOI: 10.1007/s00145-001-0017-4 J. Cryptology (2002) 15: 139–148

![](_page_0_Picture_1.jpeg)

# **Authenticated Key Exchange Provably Secure against the Man-in-the-Middle Attack**

## Anna M. Johnston

Sandia National Laboratories,∗ Albuquerque, NM 87185-1110, U.S.A. ajohnst@sandia.gov

## Peter S. Gemmell

Computer Science Department, University of New Mexico, Albuquerque, NM 87131-1386, U.S.A. gemmell@cs.unm.edu

Communicated by Ernie Brickell

Received March 2000 and revised August 2001 Online publication 23 November 2001

**Abstract.** The standard Diffie–Hellman key exchange is suseptible to an attack known as the man-in-the-middle attack. Lack of authentication in the protocol makes this attack possible. Adding separate authentication to the protocol solves the problem but adds extra transmission and computation costs. Protocols which combine the authentication with the key exchange (an authenticated key exchange) are more efficient but until now none were provably secure against the man-in-the-middle attack. This paper describes an authenticated key exchange based on the difficulty of the *q*th-root problem, a problem believed to be equivalent to the discrete logarithm problem over groups of order *q*<sup>2</sup> (where *q* is a large prime) and parallel to the square-root problem over the ring modulo *N*, where *N* is a strong two prime composite integer. We show that mounting a man-inthe-middle attack for our protocol is equivalent to breaking the Diffie–Hellman problem in the group.

**Key words.** *q*th Roots, Discrete logarithms, Key exchange, Signature scheme.

## **1. Introduction**

Astandard digital key exchange allows two parties to exchange publicly viewable data electronically, and with that data create a secret key known only by the two parties. The Diffie–Hellman key exchange does exactly this, and in general is very secure (see [4]). However, the Diffie–Hellman key exchange was not designed with any authentication. It

<sup>∗</sup> Sandia is a multiprogram laboratory operated by Sandia Corporation, a Lockheed Martin Company, for the United States Department of Energy under Contract DE-AC04-94AL85000.

is suseptible to the man-in-the-middle or impersonator attack. In this attack an adversary impersonates one of the parties. Without authentication there is no way to distinguish a friend from a foe.

Two basic methods have been used to solve this key exchange authentication problem. The first method simply adds an authentication scheme to the exchange. Public key exchange data is not accepted unless it is accompanied by a valid digital signature of the public data. Although this solves the authentication problem it adds extra transmission, computation, and data management costs to the protocol.

The second method is to modify the Diffie–Hellman key exchange such that the digital authentication is built into the exchange (see [7] and [3]). Authentication is most often added to the key exchange by incorporating a good one-way function into the key exchange. The one-way functions most often used are standard hash functions. These functions are complicated and often hard to analyze. To date, none of these authenticated key exchanges has been provably secure against the man-in-the-middle attack.

The authentication property of our key exchange is based on a relatively new hard problem. The *q*th-root problem (described below) is believed to be equivalent to the discrete logarithm problem over groups of order *q*2, where *q* is a large prime integer. This hard problem gives us a very simple one-way function: raising elements of order *q*<sup>2</sup> in the group to the *q*th power is a one-way function. The algebraic simplicity of this one-way function is what enables us to prove the security of the key exchange.

What we propose to do in this paper is to describe an authenticated key exchange provably secure against the man-in-the-middle attack. We will show that if the manin-the-middle attack can be mounted against our key exchange, then we can solve the Diffie–Hellman problem.

## **2. The** *q***th Root Problem**

The *q*th root problem (see [1] and [6]) over a group *G* of order *q*<sup>2</sup> is parallel, in many ways, to the square-root problem modulo a two prime composite. Factoring the modulus is equivalent to the ability to find square roots, and the ability to find square roots enables factoring. Likewise, solving the discrete logs problem in *G* is equivalent to the ability to find *q*th roots in *G*, and the ability to find *q*th roots enables the solving of the discrete logarithm problem (see [2]). These problems convert the hard problems of factoring and discrete logs to root-finding problems.

A few characteristics of the problems disrupt their parallelism. These characteristic differences all stem from the fact that the square-root problem is tied to the factoring problem and the *q*th-root problem is tied to the discrete log problem over *G*. Each give good and bad cryptographic traits to its particular "root" problem.

The first major difference is the choice of group. An important cryptographic implementation detail is what group will the system be working over. The choice effects run time, security, power consumption, and the amount of data necessary for transmission. For example, modulo *N* arithmetic, where *N* is a large composite integer, is complicated and time consuming. On the other hand, if the group *G* was chosen such that the base operations are over *GF*(2), much less time and effort are usually required. The squareroot problem is tied to factoring, which limits the choice of group. The *q*th-root problem is tied to the discrete logarithm problem, allowing for many choices for the group.

The second difference is the possible existence of a trapdoor. This is both a plus and minus for both groups, depending on the cryptographic requirements. When the security of a system is based on factoring, knowledge of the factors is a trapdoor. This single piece of information allows the holder to compute square roots at will. No such trapdoor exists with the qth-root problem. A trapdoor makes public key encryption and signature with message recovery possible. Without the trapdoor, designing public key encryption and signature with message recovery is difficult if not impossible. On the other hand, if only a signature is needed, then the fact that such a trapdoor does not exist lends credence to the system, especially in situations with mutually mistrusting parties.

This paper describes a simple authenticated key exchange based on the qth-root problem.

## 3. Why Is an Authenticated Key Exchange Necessary?

In a standard Diffie—Hellman key exchange (see Fig. 1), a shared secret is established by exchanging a common base element raised to a one-time random, secret value. The users create the shared secret by raising the value received by the random secret they have created. Because the exponentiation is commutative, these values will be the same for both users. However, because the discrete logarithm problem is so hard, no one other than these two users should be able to create this shared secret

The two users can now use the shared secret as a key for a symmetric cryptosystem. This technique is simple, fairly efficient, and secure. Computing the secret key from the two public portions of the key is called the Diffie–Hellman problem and it appears to be as difficult as the discrete logarithm problem.

## **Definition 1** (The Diffie–Hellman Problem). Given

- G: A cyclic group (or subgroup) for which discrete logarithms are "hard".
- $\alpha$ : A primitive element in G.
- $(\alpha^a, \alpha^b)$ : Public portions of a key exchange.

Find the secret key  $\alpha^{ab}$ . Although never proven, this problem is considered to be equivalent to the discrete logarithm problem.

![](_page_2_Figure_12.jpeg)

Fig. 1. Standard Diffie–Hellman key exchange.

<sup>&</sup>lt;sup>1</sup> The discrete logarithm problem is intractable and without trapdoors for most large groups with non-smooth order. However, there are some poor choices of groups G for which the discrete logarithm problem is subexponential—see [8] and [5].

![](_page_3_Picture_2.jpeg)

Fig. 2. Impersonation attack.

There is only one major problem with the scheme: it is not authenticated. This means that user A has no way of knowing if the  $\alpha^{r_B}$  actually came from user B. A third party (C) could have intercepted the transmission from B and substituted their own value (say  $\alpha^{r_C}$ ). User A believes that the key generated is shared with user B, when in fact it is shared with user C. Any transmissions sent by user A to B can be intercepted by user C and read. User C can also send messages to user A, posing as user B. If user C intercepts and replaces transmissions from both users (A and B), user C can effectively tap an encrypted line. Neither user would be able to tell that any thing is wrong with their system and both would believe that the messages they were sending could only be read by the other user. This attack is called the impersonation or man-in-the-middle attack (see Fig. 2).

**Definition 2** (Generalized Impersonation Attack). Let E be a key exchange protocol with public long term parameters  $P_a$ ,  $P_b$ , one-time public parameters  $D_a$ ,  $D_b$ , which returns a key K:  $E(P_a, P_b, D_a, D_b) = K$ . An impersonation attack on E computes a one-time public D' and a matching key K' given  $D_a$ ,  $P_a$ ,  $P_b$ :  $E(P_a, P_b, D_a, D') = K'$ . The attack can be reduced to finding the function F, where

$$F(P_a, D_a, P_b) = [D', K'].$$

# 4. Authenticated Key Exchange

The main purpose of an authenticated key exchange is to prevent the impersonation attack. An authenticated key exchange does not guarantee that the two parties share the same key. The two parties will share the same key only if they receive uncorrupted data from each other. An authenticated key exchange does guarantee that the two parties either

- (1) share a common key or
- (2) share no key with each other *OR* anyone else.

The impersonation attack can be thwarted in several ways. The first technique adds an authentication mechanism into the key exchange: add a digital signature of the public version of the key half. This prevents the impersonation attack at the cost of a digital signature.

A less costly solution is to use a key exchange with authentication built in: an authenticated key exchange protocol. The following scheme differs from the basic Diffie-Hellman scheme by applying a one-way function to the random value and adding a long term secret key to the scheme. In this simplified description it is assumed that each user has an authenticated public version of the other user's secret key and that the secret keys remain secret. It is described in [7] and what follows is a generalized overview:

## Components

- G: A group for which discrete logarithms are "hard".
- $\alpha$ : An element whose order is divisible by a large prime divisor.
- $x_i$ : Long term secret integer (modulo the order of  $\alpha$ ) for user i.
- $\gamma_i$ : The public version of  $x_i$ , namely  $\gamma_i \equiv \alpha^{x_i}$ .
- $r_i$ : A one-time random secret integer (modulo the order of  $\alpha$ ) for user i.
- $\mu_i$ : The public version of  $r_i$ , namely  $\mu_i \equiv \alpha^{r_i}$ .
- H: This function converts an element in G into an integer modulo the order of  $\alpha$ .

In standard Diffie-Hellman key exchange the  $\mu_i$  values are exchanged and combined with the user's one-time random secret value to obtain the final key. This scheme exchanges the same one-time public values (the  $\mu_i$  values) but combines them with the long term keys in such a way that the impersonation attack is blocked.

## **Authenticated Key Exchange** (see Fig. 3)

- 1. Transmit the  $\mu_i$  values.
- 2. Receive  $\mu_i$ .
- 3. Compute  $\theta_i \equiv \mu_j \gamma_j^{H(\mu_j)} \equiv \alpha^{x_j H(\mu_j) + r_j}$ . 4. Compute the shared key:  $\theta_i^{x_i H(\mu_i) + r_i} \equiv \alpha^{(x_i H(\mu_i) + r_i)(x_j H(\mu_j) + r_j)}$ .

Whilethe long term secret is necessary for authentication, without the one-way function on the random data (i.e., using  $\mu_i$  in the exponent) the impersonation attack would still be viable. Here is how it works. In the description below C will impersonate user A to user B:

- 1. C (the man-in-the-middle) has access to  $\gamma_A$  and prevents the true  $\mu_A$  from reaching B.
- 2. C generates a random value *t*.
- 3. Let t equal  $x_A + r'_A$ . Neither  $x_A$  nor  $r'_A$  is known.

![](_page_4_Figure_21.jpeg)

**Fig. 3.** Authenticated key exchange.

- 4. C now generates  $\mu'_A \equiv \alpha^{r'_A}$  by computing  $\mu'_A \equiv \alpha^t \gamma_A^{-1}$ .
- 5. The shared key will be  $\alpha^{t(x_B+r_B)}$ , which C creates with knowledge of t.

#### 4.1. How the Attack is Blocked

In the previous authenticated key exchange the one-way function, g, on the random public component was simple exponentiation:  $\mu_i$  is used in the exponent to create the key. An imposter would still be able to generate a random t value, but removing the public version of the long term private key and solving for the random one-time public key appears to be a very hard problem.

Given  $\gamma_A$ ,  $\gamma_B$ , and  $\mu_B$  the imposter must generate a matching pair  $\mu_C$ , K, where

$$K = \alpha^{(x_A H(\mu_C) + r_C)(x_B H(\mu_B) + r_B)}.$$

where  $r_C$  is the discrete logarithm, base  $\alpha$ , of  $\mu_C$ . The imposter can create  $\alpha^{(x_BH(\mu_B)+r_B)}$  which reduces the problem to finding a pair

$$\mu_C$$
,  $[t = x_A H(\mu_C) + r_C]$ .

Choosing a random  $r_C$  and solving for t involves solving a discrete log problem. Choosing a random t and solving for  $\mu_C$  seems more tractable. Start by generating a random  $t' = x_A + r_c H(\mu_C)^{-1}$ . This allows us to strip off the  $x_A$  in the exponent and group all the unknowns together. If  $\mu_C$  can be found, then the original t value is easily derived  $(t = t'H(\mu_C))$ .

With this data the value  $\mu_C^{H(\mu_C)^{-1}}$  can be computed. However, computing  $\mu_C$  from this value appears to be as difficult as the discrete log problem.

## 5. Simplified Authenticated Key Exchange

In order to simplify the key exchange the first question to ask is what purpose does the one-way function serve? Its main purpose is to prevent an imposter from using the public information of two legitimate users to create a key and a public value. The imposter wants the key and public value to have the property that if the public value is sent to one of the legitimate users, they will use it, along with their private key and the other legitimate user's public key, to create a key which the imposter can duplicate. This is what the second version of the impersonation attack does (see Fig. 4).

The scheme presented in this paper also uses a one-way function to thwart an impersonation attack. The one-way function is much simpler (arithmetically) however, and thus more can be proved about it. In [2] it was shown that finding qth roots in a group of order  $q^2$  was as equivalent to finding discrete logarithms in a subgroup of order q. Raising elements to the qth power in a group of order  $q^2$  is a simple one-way function based on the discrete logarithm problem, and the one we use for this simplified authenticated key exchange (see Fig. 5). The scheme is the following:

## Components

G: A group (or subgroup) for which discrete logarithms are "hard" and which has
order a<sup>2</sup>.

![](_page_6_Figure_2.jpeg)

Impersonation attack—version 2.

- $\alpha$ : An element whose order is  $q^2$ .
- $x_i$ : Long term secret integer (modulo  $q^2$ ) for user i.
- $\gamma_i$ : The public version of  $x_i$ , namely  $\gamma_i \equiv \alpha^{x_i}$ .
- $r_i$ : A one-time random secret integer (modulo  $q^2$ ) for user i.
- $\mu_i$ : The public version of  $r_i$ , namely  $\mu_i \equiv \alpha^{r_i}$ .

## Simplified Authenticated Key Exchange (SAKE)

- 1. Transmit the  $\mu_i$  values.
- 2. Receive  $\mu_i$ .
- Compute θ<sub>j</sub> ≡ μ<sub>j</sub><sup>q</sup> γ<sub>j</sub> ≡ α<sup>x<sub>j</sub>+qr<sub>j</sub></sup>.
   Compute the shared key: θ<sub>j</sub><sup>x<sub>i</sub>+qr<sub>i</sub></sup> ≡ α<sup>(x<sub>i</sub>+qr<sub>i</sub>)(x<sub>j</sub>+r<sub>j</sub>q)</sup>.

The simplicity of the one-way function has several benefits. First, it allows us to show that performing an impersonator attack on SAKE is equivalent to solving the Diffie-Hellman problem. Second, it may allow for efficiency improvements in hardware as the one-way function and exponent, q, can be chosen or designed as needed. One draw back to this scheme is that it requires a group (or subgroup) of order  $q^2$ . Finding such a group is slightly more difficult (though this is one time work) and for some groups, such as elliptic curves, it could require more transmission bits.

![](_page_6_Figure_15.jpeg)

Fig. 5. Simplified authenticated key exchange.

#### 6. Mapping to the Diffie-Hellman Problem

Although standard Diffie–Hellman key exchange is vulnerable to the impersonation attack, the fundamental Diffie–Hellman problem appears to be hard. This section shows that performing an impersonation attack against SAKE would break the Diffie–Hellman problem.

We have:

- G: A group (or subgroup) for which discrete logarithms are "hard" and which has order  $q^2$ .
- $\alpha$ : An element whose order is  $q^2$ .

An impersonation attack against SAKE (see Definition 2) implies that the attacker, knowing only  $\alpha^X$ ,  $\alpha^Y$ , and  $\alpha^Z$ , is able to generate the pair

$$[\alpha^R, K = \alpha^{(X+qZ)(Y+qR)}].$$

With this matched pair, an impersonator would send  $\alpha^R$  to the user with the secret key X. This user would think that a key had been exchanged with the user with the secret key Y. Instead the key would be shared with the impersonator. This section shows that implementing the impersonation attack is equivalent to breaking the Diffie–Hellman problem.

#### 6.1. The ORACLE

The ORACLE is a function which takes three inputed values and returns two. In particular the ORACLE is defined by the function f:

$$f(\alpha^X, \alpha^Y, \alpha^Z) = [\alpha^R, K = \alpha^{(X+qZ)(Y+qR)}].$$

6.2. The Reduction: Solving the Diffie-Hellman Problem Using the ORACLE

Given the ORACLE f, solving the Diffie–Hellman problem requires three calls to the oracle, five exponential group operations, and standard group operations.

## To Compute $\alpha^{XY}$

- 1. Choose three random values in  $\mathcal{Z}_{a^2}^*$ ,  $Z_1$ ,  $Z_2$ ,  $Z_3$ .
- 2. Call the oracle on inputs  $\alpha^X$ ,  $\alpha^Y$ , and  $\alpha^{Z_1}$ :

$$f(\alpha^X, \alpha^Y, \alpha^{Z_1}) = [\alpha^{R_1}, K_1 = \alpha^{(X+qZ_1)(Y+qR_1)} = \alpha^{XY+q(XR_1+YZ_1)}].$$

3. Call the ORACLE on inputs  $\alpha^X$ ,  $\alpha^{R_1}$ , and  $\alpha^{Z_2}$ :

$$f(\alpha^X, \alpha^{R_1}, \alpha^{Z_2}) = [\alpha^{R_2}, K_2 = \alpha^{(X+qZ_2)(R_1+qR_2)} = \alpha^{XR_1+q(XR_2+Z_2R_1)}].$$

4. Call the ORACLE on inputs  $\alpha^Y$ ,  $\alpha^{Z_1}$ , and  $\alpha^{Z_3}$ :

$$f(\alpha^Y, \alpha^{Z_1}, \alpha^{Z_3}) = [\alpha^{R_3}, K_3 = \alpha^{(Y+qZ_3)(Z_1+qR_3)} = \alpha^{YZ_1+q(YR_3+Z_3Z_1)}].$$

5. Raise  $K_2$  and  $K_3$  to the -q power to obtain

$$K_2^{-q} = \alpha^{-qXR_1},$$
  
$$K_2^{-q} = \alpha^{-qYZ_1}.$$

6. Multiply  $K_1$ ,  $K_2^{-q}$ , and  $K_3^{-q}$  to obtain the Diffie–Hellman value:

$$K_1K_2^{-q}K_2^{-q} = \alpha^{XY+q(XR_1+YZ_1)-q(XR_1+YZ_1)} = \alpha^{XY}.$$

## 6.3. Conclusions of the Proof

With the imposter ORACLE and the public versions of the key, the Diffie–Hellman problem can be easily broken. This shows breaking SAKE with an imposter attack is as difficult as breaking the Diffie–Hellman problem.

#### 7. Conclusions

The SAKE algorithm provides a simple, authenticated method for exchanging keys which is provably secure against an imposter attack. The algorithm is flexible: it works over any group for which discrete logarithms are difficult and the square of a large prime divides the order. For example, various elliptic curve or  $F_P$  are suitable.

Another benefit is that the prime q is fixed, allowing for easy optimization of the implementation. The group can even be created with a particular prime q in mind. A prime with low bit density will improve the efficiency.

#### References

- E. Bach and J. Shallit, Algorithmic Number Theory Volume 1: Efficient Algorithms, second edn., MIT Press, Cambridge, MA, 1997.
- [2] C. Beaver, P. Gemmell, A. Johnston, and W. Newmann, On the cryptographic value of the qth-root problem, in Proceedings of the International Conference on Information and Computer Security, Lecture Notes in Computer Science, Springer-Verlag, Berlin, 1999, pp. 135–142.
- [3] S. M. Bellovin and M. Merritt, Encrypted key exchange: password-based protocols secure against dictionary attacks, in *Proceedings of the IEEE Computer Society Symposium on Research in Security and Privacy*, May 1992, pp. 72–84.
- [4] W. Diffie and M. Hellman, New directions in cryptography, in *IEEE Transactions on Information Theory*, vol. 22 (November 1976), pp. 644–654.
- [5] G. Frey and H.-G. Rück, A remark concerning m-divisibility and the discrete logarithm in the divisor class group of curves, Mathematics of Computation, vol. 62 (1994), pp. 865–874.
- [6] A. Johnston, A generalized qth-root algorithm, in Proceedings of the Tenth Annual ACM-SIAM Symposium on Discrete Algorithms, January 1999.
- [7] L. Law, A. Menezes, M. Qu, J. Solinas, and S. Vanstone, An Efficient Protocol for Authenticated Key Agreement, Technical Report CORR 98-05, Department of C&O, University of Waterloo, Ontario, March 1998.
- [8] A. Menezes, T. Okamoto, and S. Vanstone, Reducing elliptic curve logarithms to logarithms in a finite field, in *Proceedings of the 23rd Annual ACM Symposium on Theory of Computing*, 1991, pp. 80–89.

- [9] M. O. Rabin, Digitalized Signatures and Public Key Functions as Intractable as Factorization. Report MIT/LCS/TR-212, MIT Laboratory for Computer Science, Cambridge, MA, 1979.
- [10] K. H. Rosen, *Elementary Number Theory and its Applications*, Addison-Wesley, Reading, MA, third edn., 1993.
- [11] D. Shanks, Five number-theoretic algorithms, in *Proceedings of the Second Manitoba Conference on Numerical Mathematics*, no. VII, 1972, pp. 51–70.
```

## File: references/Measuring Small Subgroup Attacks Against Diffie-Hellman.md
```markdown
# Measuring small subgroup attacks against Diffie-Hellman

Luke Valenta\*, David Adrian<sup>†</sup>, Antonio Sanso<sup>‡</sup>, Shaanan Cohney\*, Joshua Fried\*, Marcella Hastings\*, J. Alex Halderman<sup>†</sup>, Nadia Heninger\*

\*University of Pennsylvania

<sup>†</sup>University of Michigan

<sup>‡</sup>Adobe

Abstract-Several recent standards, including NIST SP 800-56A and RFC 5114, advocate the use of "DSA" parameters for Diffie-Hellman key exchange. While it is possible to use such parameters securely, additional validation checks are necessary to prevent well-known and potentially devastating attacks. In this paper, we observe that many Diffie-Hellman implementations do not properly validate key exchange inputs. Combined with other protocol properties and implementation choices, this can radically decrease security. We measure the prevalence of these parameter choices in the wild for HTTPS, POP3S, SMTP with STARTTLS, SSH, IKEv1, and IKEv2, finding millions of hosts using DSA and other non-"safe" primes for Diffie-Hellman key exchange, many of them in combination with potentially vulnerable behaviors. We examine over 20 open-source cryptographic libraries and applications and observe that until January 2016, not a single one validated subgroup orders by default. We found feasible full or partial key recovery vulnerabilities in OpenSSL, the Exim mail server, the Unbound DNS client, and Amazon's load balancer, as well as susceptibility to weaker attacks in many other applications.

## I. INTRODUCTION

Diffie-Hellman key exchange is one of the most common public-key cryptographic methods in use in the Internet. It is a fundamental building block for IPsec, SSH, and TLS. In the textbook presentation of finite field Diffie-Hellman, arda and burak agree on a large prime p and an integer g modulo p. arda chooses a secret integer  $x_a$  and transmits a public value  $g^{x_a} \mod p$ ; burak chooses a secret integer  $x_b$  and transmits his public value  $g^{x_b} \mod p$ . Both arda and burak can reconstruct a shared secret  $g^{x_a x_b} \mod p$ , but the best known way for a passive eavesdropper to reconstruct this secret is to compute the discrete log of either arda or burak's public value. Specifically, given g, p, and  $g^x \mod p$ , an attacker must calculate x.

In order for the discrete log problem to be hard, Diffie-Hellman parameters must be chosen carefully. A typical recommendation is that p should be a "safe" prime, that is, that p=2q+1 for some prime q, and that q should generate the group of order q modulo q. For q that are not safe, the group order q can be much smaller than q. For security, q must still

Permission to freely reproduce all or part of this paper for noncommercial purposes is granted provided that copies bear this notice and the full citation on the first page. Reproduction for commercial purposes is strictly prohibited without the prior written consent of the Internet Society, the first-named author (for reproduction of an entire paper only), and the author's employer if the paper was prepared within the scope of employment.

NDSS'17, 26 February–1 March, 2017, San Diego, CA, USA Internet Society, ISBN 1-891562-46-0 http://dx.doi.org/10.14722/ndss.2017.23171

be large enough to thwart known attacks, which for prime q run in time  $O(\sqrt{q})$ . A common parameter choice is to use a 160-bit q with a 1024-bit p or a 224-bit q with a 2048-bit p, to match the security level under different cryptanalytic attacks. Diffie-Hellman parameters with p and q of these sizes were suggested for use and standardized in DSA signatures [50]. For brevity, we will refer to these non-safe primes as DSA primes, and to groups using DSA primes with smaller values of q as DSA groups.

A downside of using DSA primes instead of safe primes for Diffie-Hellman is that implementations must perform additional validation checks to ensure the key exchange values they receive from the other party are contained in the correct subgroup modulo p. The validation consists of performing an extra exponentiation step. If implementations fail to validate, a 1997 attack of Lim and Lee [54] can allow an attacker to recover a static exponent by repeatedly sending key exchange values that are in very small subgroups. We describe several variants of small subgroup confinement attacks that allow an attacker with access to authentication secrets to mount a much more efficient man-in-the-middle attack against clients and servers that do not validate group orders. Despite the risks posed by these well-known attacks on DSA groups, NIST SP 800-56A, "Recommendations for Pair-Wise Key Establishment Schemes Using Discrete Logarithm Cryptography" [23] specifically recommends DSA group parameters for Diffie-Hellman, rather than recommending using safe primes. RFC 5114 [53] includes several DSA groups for use in IETF standards.

We observe that few Diffie-Hellman implementations actually validate subgroup orders, in spite of the fact that small subgroup attacks and countermeasures are well-known and specified in every standard suggesting the use of DSA groups for Diffie-Hellman, and DSA groups are commonly implemented and supported in popular protocols. For some protocols, including TLS and SSH, that enable the server to unilaterally specify the group used for key exchange, this validation step is not possible for clients to perform with DSA primes—there is no way for the server to communicate to the client the intended order of the group. Many standards involving DSA groups further suggest that the order of the subgroup should be matched to the length of the private exponent. Using shorter private exponents yields faster exponentiation times, and is a commonly implemented optimization. However, these standards provide no security justification for decreasing the size of the subgroup to match the size of the exponents, rather than using as large a subgroup as possible. We discuss possible motivations for these recommendations later in the paper.

We conclude that adopting the Diffie-Hellman group recommendations from RFC 5114 and NIST SP 800-56A may create vulnerabilities for organizations using existing cryptographic implementations, as many libraries allow user-configurable groups but have unsafe default behaviors. This highlights the need to consider developer usability and implementation fragility when designing or updating cryptographic standards.

**Our Contributions.** We study the implementation landscape of Diffie-Hellman from several perspectives and measure the security impact of the widespread failure of implementations to follow best security practices:

- We summarize the concrete impact of small-subgroup confinement attacks and small subgroup key recovery attacks on TLS, IKE, and SSH handshakes.
- We examined the code of a wide variety of cryptographic libraries to understand their implementation choices. We find feasible full private exponent recovery vulnerabilities in OpenSSL and the Unbound DNS resolver, and a partial private exponent recovery vulnerability for the parameters used by the Amazon Elastic Load Balancer. We observe that no implementation that we examined validated group order for subgroups of order larger than two by default prior to January 2016, leaving users potentially vulnerable to small subgroup confinement attacks.
- We performed Internet-wide scans of HTTPS, POP3S, SMTP with STARTTLS, SSH, IKEv1, and IKEv2, to provide a snapshot of the deployment of DSA groups and other non-"safe" primes for Diffie-Hellman, quantify the incidence of repeated public exponents in the wild, and quantify the lack of validation checks even for safe primes.
- We performed a best-effort attempt to factor p-1 for all non-safe primes that we found in the wild, using ~100,000 core-hours of computation. Group 23 from RFC 5114, a 2048-bit prime, is particularly vulnerable to small subgroup key recovery attacks; for TLS a full key recovery requires  $2^{33}$  online work and  $2^{47}$  offline work to recover a 224-bit exponent.

Disclosure and Mitigations. We reported the small subgroup key recovery vulnerability to OpenSSL in January 2016 [66]. OpenSSL issued a patch to add additional validation checks and generate single-use private exponents by default [11]. We reported the Amazon load balancer vulnerability in November 2015. Amazon responded to our report informing us that they have removed Diffie-Hellman from their recommmended ELB security policy, and have reached out to their customers to recommend that they use these latest policies. Based on scans performed in February and May 2016, 88% of the affected hosts appear to have corrected their exponent generation behavior. We found several libraries that had vulnerable combinations of behaviours, including Unbound DNS, GnuTLS, LibTomCrypt, and Exim. We disclosed to the developers of these libraries. Unbound issued a patch, GnuTLS acknowledged the report but did not patch, and LibTomCrypt did not respond. Exim responded to our bug report stating that they would use their own generated Diffie-Hellman groups by default, without specifying subgroup order for validation [10], [12]. We found products from Cisco, Microsoft, and VMWare lacking validation that key exchange values were in the range (1, p - 1). We informed these companies, and discuss their responses in Section III-D.

## II. BACKGROUND

<span id="page-1-0"></span>

### A. Groups, orders, and generators

The two types of groups used for Diffie-Hellman key exchange in practice are multiplicative groups over finite fields ("mod p") and elliptic curve groups. We focus on the "mod p" case, so a group is typically specified by a prime p and a generator g, which generates a multiplicative subgroup modulo p. Optionally, the group order q can be specified; this is the smallest positive integer q satisfying  $g^q \equiv 1 \mod p$ . Equivalently, it is the number of distinct elements of the subgroup  $\{g, g^2, g^3, \dots \mod p\}$ .

By Lagrange's theorem, the order q of the subgroup generated by g modulo p must be a divisor of p-1. Since p is prime, p-1 will be even, and there will always be a subgroup of order 2 generated by the element -1. For the other factors  $q_i$  of p-1, there are subgroups of order  $q_i \mod p$ . One can find a generator  $g_i$  of a subgroup of order  $q_i$  using a randomized algorithm: try random integers h until  $h^{(p-1)/q_i} \neq 1 \mod p$ ;  $g_i = h^{(p-1)/q_i} \mod p$  is a generator of the subgroup. A random h will satisfy this property with probability  $1 - 1/q_i$ .

In theory, neither p nor q is required to be prime. Diffie-Hellman key exchange is possible with a composite modulus and with a composite group order. In such cases, the order of the full multiplicative group modulo p is  $\phi(p)$  where  $\phi$  is Euler's totient function, and the order of the subgroup generated by g must divide  $\phi(p)$ . Outside of implementation mistakes, Diffie-Hellman in practice is done modulo prime p.

### B. Diffie-Hellman Key Exchange

Diffie-Hellman key exchange allows two parties to agree on a shared secret in the presence of an eavesdropper [29]. arda and burak begin by agreeing on shared parameters (prime p, generator g, and optionally group order q) for an algebraic group. Depending on the protocol, the group may be requested by the initiator (as in IKE), unilaterally chosen by the responder (as in TLS), or fixed by the protocol itself (SSH originally built in support for a single group).

Having agreed on a group, arda chooses a secret  $x_a < q$  and sends burak  $y_a = g^{x_a} \mod p$ . Likewise, burak chooses a secret  $x_b < q$  and sends arda  $y_b = g^{x_b} \mod p$ . Each participant then computes the shared secret key  $g^{x_a x_b} \mod p$ .

Depending on the implementation, the public values  $y_a$  and  $y_b$  might be *ephemeral*—freshly generated for each connection—or *static* and reused for many connections.

### C. Discrete log algorithms

The best known attack against Diffie-Hellman is for the eavesdropper to compute the the private exponent x by calculating the discrete log of one of arda or burak's public value y. With knowledge of the exponent, the attacker can trivially compute the shared secret. It is not known in general whether the hardness of computing the shared secret from the public values is equivalent to the hardness of discrete log.

The computational Diffie-Hellman assumption states that computing the shared secret  $g^{x_ax_b}$  from  $g^{x_a}$  and  $g^{x_b}$  is hard for some choice of groups. A stronger assumption, the decisional Diffie-Hellman problem, states that given  $g^{x_a}$  and  $g^{x_b}$ , the shared secret  $g^{x_ax_b}$  is computationally indistinguishable from random for some groups. This assumption is often not true for groups used in practice; even with safe primes as defined below, many implementations use a generator that generates

the full group of order p-1, rather than the subgroup of order (p-1)/2. This means that a passive attacker can always learn the value of the secret exponent modulo 2. To avoid leaking this bit of information about the exponent, both sides could agree to compute the shared secret as  $y^{2x} \mod p$ . We have not seen implementations with this behavior.

There are several families of discrete log algorithms, each of which apply to special types of groups and parameter choices. Implementations must take care to avoid choices vulnerable to any particular algorithm. These include:

**Small-order groups.** The Pollard rho [63] and Shanks' baby step-giant step algorithms [67] each can be used to compute discrete logs in groups of order q in time  $O(\sqrt{q})$ . To avoid being vulnerable, implementations must choose a group order with bit length at least twice the desired bit security of the key exchange. In practice, this means that group orders q should be at least 160 bits for an 80-bit security level.

Composite-order groups. If the group order q is a composite with prime factorization  $q = \prod_i q_i^{e_i}$ , then the attacker can use the Pohlig-Hellman algorithm [61] to compute a discrete log in time  $O(\sum_i e_i \sqrt{q_i})$ . The Pohlig-Hellman algorithm computes the discrete log in each subgroup of order  $q_i^{e_i}$  and then uses the Chinese remainder theorem to reconstruct the log modulo q. Adrian et al. [18] found several thousand TLS hosts using primes with composite-order groups, and were able to compute discrete logs for several hundred Diffie-Hellman key exchanges using this algorithm. To avoid being vulnerable, implementations should choose g so that it generates a subgroup of large prime order modulo p.

**Short exponents.** If the secret exponent  $x_a$  is relatively small or lies within a known range of values of a relatively small size, m, then the Pollard lambda "kangaroo" algorithm [64] can be used to find  $x_a$  in time  $O(\sqrt{m})$ . To avoid this attack, implementations should choose secret exponents to have bit length at least twice the desired security level. For example, using a 256-bit exponent for for a 128-bit security level.

**Small prime moduli.** When the subgroup order is not small or composite, and the prime modulus p is relatively large, the fastest known algorithm is the number field sieve [40], which runs in subexponential time in the bit length of p,  $\exp\left((1.923+o(1))(\log p)^{1/3}(\log\log p)^{2/3}\right)$ . Adrian et al. recently applied the number field sieve to attack 512-bit primes in about 90,000 core-hours [18], and they argue that attacking 1024-bit primes—which are widely used in practice—is within the resources of large governments. To avoid this attack, current recommendations call for p to be at least 2048 bits [21]. When selecting parameters, implementers should ensure all attacks take at least as long as the number field sieve for their parameter set.

### D. Diffie-Hellman group characteristics

"Safe" primes. In order to maximize the size of the subgroup used for Diffie-Hellman, one can choose a p such that p=2q+1 for some prime q. Such a p is called a "safe" prime, and q is a Sophie Germain prime. For sufficiently large safe primes, the best attack will be solving the discrete log using the number field sieve. Many standards explicitly specify the use of safe primes for Diffie-Hellman in practice. The Oakley protocol [59] specified five "well-known" groups for Diffie-Hellman in 1998. These included three safe primes of size 768, 1024, and 1536

bits, and was later expanded to include six more groups in 2003 [51]. The Oakley groups have been built into numerous other standards, including IKE [43] and SSH [71].

**DSA groups.** The DSA signature algorithm [50] is also based on the hardness of discrete log. DSA parameters have a subgroup order q of much smaller size than p. In this case p-1=qr where q is prime and r is a large composite, and g generates a group of order q. FIPS 186-4 [50] specifies 160-bit q for 1024-bit p and 224- or 256-bit q for 2048-bit p. The small size of the subgroup allows the signature to be much shorter than the size of p.

### E. DSA Group Standardization

DSA-style parameters have also been recommended for use for Diffie-Hellman key exchange, NIST Special Publication 800-56A, "Recommendation for Pair-Wise Key Establishment Schemes Using Discrete Logarithm Cryptography" [23], first published in 2007, specifies that finite field Diffie-Hellman should be done over a prime-order subgroup q of size 160 bits for a 1024-bit prime p, and a 224- or 256-bit subgroup for a 2048-bit prime. While the order of the multiplicative subgroups is in line with the hardness of computing discrete logs in these subgroups, no explanation is given for recommending a subgroup of precisely this size rather than setting a minimum subgroup size or using a safe prime. Using a shorter exponent will make modular exponentiation more efficient, but the order of the subgroup q does not increase efficiency—on the contrary, the additional modular exponentiation required to validate that a received key exchange message is contained in the correct subgroup will render key exchange with DSA primes less efficient than using a "safe" prime for the same exponent length. Choosing a small subgroup order is not known to have much impact on other cryptanalytic attacks, although the number field sieve is somewhat (not asymptotically) easier as the linear algebra step is performed modulo the subgroup order q. [18]

RFC 5114, "Additional Diffie-Hellman Groups for Use with IETF Standards" [53], specifies three DSA groups with the above orders "for use in IKE, TLS, SSH, etc." These groups were taken from test data published by NIST [1]. They have been widely implemented in IPsec and TLS, as we will show below. We refer to these groups as Group 22 (1024-bit group with 160-bit subgroup), Group 23 (2048-bit group with 224-bit subgroup), and Group 24 (2048-bit group with 256-bit subgroup) throughout the remainder of the paper to be consistent with the group numbers assigned for IKE.

RFC 6989, "Additional Diffie-Hellman Tests for the Internet Key Exchange Protocol Version 2 (IKEv2)" [68], notes that "mod p" groups with small subgroups can be vulnerable to small subgroup attacks, and mandates that IKE implementations should validate that the received value is in the correct subgroup or never repeat exponents.

<span id="page-2-0"></span>

### F. Small subgroup attacks

Since the security of Diffie-Hellman relies crucially on the group parameters, implementations can be vulnerable to an attacker who provides maliciously generated parameters that change the properties of the group. With the right parameters and implementation decisions, an attaker may be able to efficiently determine the Diffie-Hellman shared secret. In some cases, a passive attacker may be able to break a transcript offline.

Small subgroup confinement attacks. In a small subgroup confinement attack, an attacker (either a man-in-the-middle or a malicious client or server) provides a key-exchange value y that lies in a subgroup of small order. This forces the other party's view of the shared secret,  $y^x$ , to lie in the subgroup generated by the attacker. This type of attack was described by van Oorschot and Wiener [69] and ascribed to Vanstone and Anderson and Vaudenay [20]. Small subgroup confinement attacks are possible even when the server does not repeat exponents—the only requirement is that an implementation does not validate that received Diffie-Hellman key exchange values are in the correct subgroup.

When working  $\operatorname{mod} p$ , there is always a subgroup of order 2, since p-1 is even. A malicious client Mallory could initiate a Diffie-Hellman key exchange value with arda and send her the value  $y_M = p-1 \equiv -1 \mod p$ , which is is a generator of the group of order  $2 \mod p$ . When arda attempts to compute her view of the shared secret as  $k_a = y_M^a \mod p$ , there are only two possible values, 1 and  $-1 \mod p$ .

The same type of attack works if p-1 has other small factors  $q_i$ . Mallory can send a generator  $g_i$  of a group of order  $q_i$  as her Diffie-Hellman key exchange value. arda's view of the shared secret will be an element of the subgroup of order  $q_i$ . Mallory then has a  $1/q_i$  chance of blindly guessing arda's shared secret in this invalid group. Given a message from arda encrypted using arda's view of the shared secret, Mallory can brute force arda's shared secret in  $q_i$  guesses.

More recently, Bhargavan and Delignat-Lavaud [25] describe "key synchronization" attacks against IKEv2 where a man-in-the-middle connects to both the initiator and responder in different connections, uses a small subgroup confinement attack against both, and observes that there is a  $1/q_i$  probability of the shared secrets being the same in both connections. Bhargavan and Leurent [26] describe several attacks that use subgroup confinement attacks to obtain a transcript collision and break protocol authentication.

To protect against subgroup confinement attacks, implementations should use prime-order subgroups with known subgroup order. Both parties must validate that the key exchange values they receive are in the proper subgroup. That is, for a known subgroup order q, a received Diffie-Hellman key exchange value y should satisfy  $y^q \equiv 1 \mod p$ . For a safe prime, it suffices to check that y is strictly between 1 and p-1.

**Small subgroup key recovery attacks.** Lim and Lee [54] discovered a further attack that arises when an implementation fails to validate subgroup order and resues a static secret exponent for multiple key exchanges. A malicious party may be able to perform multiple subgroup confinement attacks for different prime factors  $q_i$  of p-1 and then use the Chinese remainder theorem to reconstruct the static secret exponent.

The attack works as follows. Let p-1 have many small factors  $p-1=q_1q_2\dots q_n$ . Mallory, a malicious client, uses the procedure described in Section II-A to find a generator of the subgroup  $g_i$  of order  $q_i \mod p$ . Then Mallory transmits  $g_i$  as her Diffie-Hellman key exchange value, and receives a message encrypted with arda's view of the shared secret  $g_i^{x_a}$ , which Mallory can brute force to learn the value of  $x_a \mod q_i$ . Once Mallory has repeated this process several times, she can use the Chinese remainder theorem to reconstruct  $x_a \mod \prod_i q_i$ . The running time of this attack is  $\sum_i q_i$ , assuming that Mallory performs an offline brute-force search for each subgroup.

<span id="page-3-0"></span>

| Application | Crypto<br>Library | Short<br>Exponent | Exponent<br>Reuse |
|-------------|-------------------|-------------------|-------------------|
| OpenSSH     | OpenSSL           | No                | No                |
| Cerberus    | OpenSSL           | No                | Yes               |
| GNU 1sh     | GnuTLS            | No                | No                |
| Dropbear    | LibTomCrypt       | No                | No                |
| Lighttpd    | OpenSSL           | Yes               | No                |
| Unbound     | OpenSSL           | Yes               | Yes               |
| Exim        | OpenSSL           | Library dependent | Yes               |
| Postfix     | OpenSSL           | No                | No                |

TABLE I: **Common application behavior**—Applications make a diverse set of decisions on how to handle Diffie-Hellman exponents, likely due to the plethora of conflicting, confusing, and incorrect recommendations available.

A randomly chosen prime p is likely to have subgroups of large enough order that this attack is infeasible to carry out for all subgroups. However, if in addition arda's secret exponent  $x_a$  is small, then Mallory only needs to carry out this attack for a subset of subgroups of orders  $q_1, \ldots, q_k$  satisfying  $\prod_{i=0}^k q_i > x_a$ , since the Chinese remainder theorem ensures that  $x_a$  will be uniquely defined. Mallory can also improve on the running time of the attack by taking advantage of the Pollard lambda algorithm. That is, she could use a small subgroup attack to learn the value of  $x_a \mod \prod_{i=1}^k q_i$  for a subset of subgroups  $\prod_{i=1}^k q_i < x_a$ , and then use the Pollard lambda algorithm to reconstruct the full value of a, as it has now been confined to a smaller interval.

In summary, an implementation is vulnerable to small subgroup key recovery attacks if it does not verify that received Diffie-Hellman key exchange values are in the correct subgroup; uses a prime p such that p-1 has small factors; and reuses Diffie-Hellman secret exponent values. The attack is made even more practical if the implementation uses small exponents.

A related attack exists for elliptic curve groups: an invalid curve attack. Similarly to the case we describe above, the attacker generates a series of elliptic curve points of small order and sends these points as key exchange messages to the victim. If the victim does not validate that the received point is on the intended curve, they return a response that reveals information about the secret key modulo different group orders. After enough queries, the attacker can learn the victim's entire secret. Jager, Schwenk, and Somorovsky [45] examined eight elliptic curve implementations and discovered two that failed to validate the received curve point. For elliptic curve groups, this attack can be much more devastating because the attacker has much more freedom in generating different curves, and can thus find many different small prime order subgroups. For the finite field Diffie-Hellman attack, the attacker is limited only to those subgroups whose orders are factors of p-1.

# III. TLS

<span id="page-3-1"></span>TLS (Transport Layer Security) is a transport layer protocol designed to provide confidentiality, integrity and (most commonly) one-side authentication for application sessions. It is widely used to protect HTTP and mail protocols.

A TLS client initiates a TLS handshake with the Client-Hello message. This message includes a list of supported

cipher suites, and a client random nonce  $r_c$ . The server responds with a ServerHello message containing the chosen cipher suite and server random nonce  $r_s$ , and a Certificate message that includes the server's X.509 certificate. If the server selects a cipher suite using ephemeral Diffie-Hellman key exchange, the server additionally sends a ServerKeyExchange message containing the server's choice of Diffie-Hellman parameters p and g, the server's Diffie-Hellman public value  $y_s = g^{x_s} \mod p$ , a signature by the server's private key over both the client and server nonces  $(r_c \text{ and } r_s)$ , and the server's Diffie-Hellman parameters  $(p_s)$  $g_s$ , and  $y_s$ ). The client then verifies the signature using the public key from the server's certificate, and responds with a ClientKeyExchange message containing the client's Diffie-Hellman public value  $y_c = g^{x_c} \mod p$ . The Diffie-Hellman shared secret  $Y = g^{x_s x_c} \mod p$  is used to derive encryption and MAC keys. The client then sends ChangeCipherSpec and Finished messages. The Finished message contains a hash of the handshake transcript, and is encrypted and authenticated using the derived encryption and MAC keys. Upon decrypting and authenticating this message, the server verifies that the hash of the transcript matches the expected hash. Provided the hash matches, the server then sends its own ChangeCipherSpec and Finished messages, which the client then verifies. If either side fails to decrypt or authenticate the Finished messages, or if the transcript hashes do not match, the connection fails immediately [28].

TLS also specifies a mode of using Diffie-Hellman with fixed parameters from the server's certificate [62]. This mode is not forward secret, was never widely adopted, and has been removed from all modern browsers due to dangerous protocol flaws [44]. The only widely used form of Diffie-Hellman in TLS today is ephemeral Diffie-Hellman, described above.

<span id="page-4-0"></span>

## A. Small Subgroup Attacks in TLS

Small subgroup confinement attacks. A malicious TLS server can perform a variant of the small subgroup attack against a client by selecting group parameters g and p such that g generates an insecure group order. TLS versions prior to 1.3 give the server complete liberty to choose the group, and they do not include any method for the server to specify the desired group order q to the client. This means a client has no feasible way to validate that the group sent by the server has the desired level of security or that a server's key exchange value is in the correct group for a non-safe prime.

Similarly, a man in the middle with knowledge of the server's long-term private signing key can use a small subgroup confinement attack to more easily compromise perfect forward secrecy, without having to rewrite an entire connection. The attack is similar to the those described by Bhargavan and Delignat-Lavaud [25]. The attacker modifies the server key exchange message, leaving the prime unchanged, but substituting a generator  $g_i$  of a subgroup of small order  $q_i$  for the group generator and  $g_i$  for the server's key exchange value  $y_s$ . The attacker then forges a correct signature for the modified server key exchange message and passes it to the client. The client then responds with a client key exchange message  $y_c = g_i^{x_c} \mod p$ , which the man-in-the-middle leaves unchanged. The server's view of the shared secret is then  $g_i^{x_c x_s} \mod p$ , and the client's view of the shared secret is  $g_i^{x_c} \mod p$ . These views are identical when  $x_s \equiv 1 \mod q_i$ ,

so this connection will succeed with probability  $1/q_i$ . For small enough  $q_i$ , this enables a man in the middle to use a compromised server signing key to decrypt traffic from forward-secret ciphersuites with a reasonable probability of success, while only requiring tampering with a single handshake message, rather than having to actively rewrite the entire connection for the duration of the session.

Furthermore, if the server uses a static Diffie-Hellman key exchange value, then the attacker can perform a small subgroup key-recovery attack as the client in order to learn the server's static exponent  $x_s \mod q_i$  for the small subgroup. This enables the attacker to calculate a custom generator such that the client and server views of the shared secret are always identical, raising the above attack to a 100% probability of success.

Small subgroup key recovery attacks. In TLS, the client must authenticate the handshake before the server, by providing a valid Finished message. This forces a small subgroup key recovery attack against TLS to be primarily online. To perform a Lim-Lee small subgroup key recovery attack against a server static exponent, a malicious client initiates a TLS handshake and sends a generator  $q_i$  of a small subgroup of order  $q_i$  as its client key exchange message  $y_c$ . The server will calculate  $Y_s = g_i^{x_s} \mod p$  as the shared secret. The server's view of the shared secret is confined to the subgroup of order  $q_i$ . However, since  $g_i$  and g generate separate subgroups, the server's public value  $y_s = g_s^x$  gives the attacker no information about the value of the shared secret  $Y_s$ . Instead, the attacker must guess a value for  $x_s \mod q_i$ , and send the corresponding client Finished message. If the server continues the handshake, the attacker learns that the guess is correct. Therefore, assuming the server is reusing a static value for  $x_s$ , the attacker needs to perform at most  $q_i$  queries to learn the server's secret  $x_s \mod q_i$  [54]. This attack is feasible if  $q_i$  is small enough and the server reuses Diffie-Hellman exponents for sufficiently many requests.

The attacker repeats this process for many different primes  $q_i$ , and uses the Chinese remainder theorem to combine them modulo the product of the primes  $q_i$ . The attacker can also use the Pollard lambda algorithm to reconstruct any remaining bits of the exponent [54].

We note that the TLS False Start extension allows the server to send application data before receiving the client's authentication [52]. The specification only allows this behavior for abbreviated handshakes, which do not include a full key exchange. If a full key exchange were allowed, the fact that the server authenticates first would allow a malicious client to mount a mostly offline key recovery attack.

## B. OpenSSL

Prior to early 2015, OpenSSL defaulted to using static-ephemeral Diffie-Hellman values. Server applications generate a fresh Diffie-Hellman secret exponent on startup, and reuse this exponent until they are restarted. A server would be vulnerable to small subgroup attacks if it chose a DSA prime, explicitly configured the dh->length parameter to generate a short exponent, and failed to set SSL\_OP\_SINGLE\_DH\_USE to prevent repeated exponents. OpenSSL provides some test code for key generation which configures DSA group parameters, sets an exponent length to the group order, and correctly sets the SSL\_OP\_SINGLE\_DH\_USE to generate new exponents on every connection. We found this test code widely used across many applications. We discovered that Unbound, a DNS

<span id="page-5-1"></span>

| Implementation | RFC 5114 Support      | Allows Short Exponents                         | Reuses Exponents      | Validates Subgroup |
|----------------|-----------------------|------------------------------------------------|-----------------------|--------------------|
| Mozilla NSS    | No                    | Yes, hardcoded                                 | No                    | $g \leq 2$         |
| OpenJDK        | No                    | Yes, uses max of p_size / 2 and 384            | No                    | $g \leq 2$         |
| OpenSSL 1.0.2  | Yes                   | Yes, if q set or if user sets a shorter length | Default until Jan '16 | Yes, as of Jan '16 |
| BouncyCastle   | Yes                   | No                                             | Application dependent | $g \leq 2$         |
| Cryptlib       | No                    | Yes, uses quadratic curve calculation          | Application dependent | $g \leq 2$         |
| libTomCrypt    | No                    | Yes, hardcoded                                 | Application dependent | No                 |
| CryptoPP       | No                    | Yes, uses work factor calculation              | Application dependent | No                 |
| Botan          | Yes                   | Yes, uses work factor calculation              | No                    | No                 |
| GnuTLS         | Application dependent | Yes, restricts to q_size (max 256)             | Application dependent | No                 |

TABLE II: **TLS Library Behavior**—We examined popular TLS libraries to determine which weaknesses from Section II-F were present. Reuse of exponents often depends on the use of the library; the burden is on the application developer to appropriately regenerate exponents. Botan and libTomCrypt both hardcode their own custom groups, while GnuTLS allows users to specify their own parameters.

resolver, used the same parameters as the tests, but without setting SSL\_OP\_SINGLE\_DH\_USE, rendering them vulnerable to a key recovery attack. A number of other applications including Lighttpd used the same or similar code with non-safe primes, but correctly set SSL\_OP\_SINGLE\_DH\_USE.

In spring 2015, OpenSSL added explicit support for RFC 5114 groups [6], including the ability for servers to specify a subgroup order in a set of Diffie-Hellman group parameters. When the subgroup order is specified, the exponent length is automatically adjusted to match the subgroup size. However, the update did not contain code to validate subgroup order for key exchange values, leaving OpenSSL users vulnerable to precisely the key recovery attack outlined in Section III-A.

We disclosed this vulnerability to OpenSSL in January 2016. The vulnerability was patched by including code to validate subgroup order when a subgroup was specified in a set of Diffie-Hellman parameters and setting SSL\_OP\_SINGLE\_DH\_USE by default [15]. Prior to this patch, any code using OpenSSL for DSA-style Diffie-Hellman parameters was vulnerable to small subgroup attacks by default.

Exim [4], a popular mail server that uses OpenSSL, provides a clear example of the fragile situation created by this update. By default, Exim uses the RFC 5114 Group 23 parameters with OpenSSL, does not set an exponent length, and does not set SSL\_OP\_SINGLE\_DH\_USE. In a blog post, an Exim developer explains that because of "numerous issues with automatic generation of DH parameters", they added support for fixed groups specified in RFCs and picked Group 23 as the default [12]. Exim narrowly avoided being fully vulnerable to a key recovery attack by not including the size of the subgroup generated by q in the Diffie-Hellman parameters that it passes to OpenSSL. Had this been included, OpenSSL would have automatically shortened the exponent length, leaving the server fully vulnerable to a key recovery attack. For this group, an attacker can recover 130 bits of information about the secret exponent using  $2^{33}$  online queries, but this does not allow the attacker to recover the server's 2048-bit exponent modulo the correct 224-bit group order q as the small subgroup orders  $q_i$ are all relatively prime to q.

We looked at several other applications as well, but did not find them to be vulnerable to key recovery attacks (Table I).

<span id="page-5-2"></span>

## C. Other Implementations

We examined the source code of multiple TLS implementations (Table II). Prior to January 2016, no TLS implementations

that we examined validated group order, even for the well-known DSA primes from RFC 5114, leaving them vulnerable to small subgroup confinement attacks.

Most of the implementations we examined attempt to match exponent length to the perceived strength of the prime. For example, Mozilla Network Security Services (NSS), the TLS library used in the Firefox browser and some versions of Chrome [7], [36], uses NIST's "comparable key strength" recommendations on key management [21], [22] to determine secret exponent lengths from the length of the prime. [2] Thus NSS uses 160-bit exponents with a 1024-bit prime, and 224-bit exponents with a 2048-bit prime. In fall 2015, NSS added an additional check to ensure that the shared secret  $q^{x_a x_b} \not\equiv 1 \mod p$  [5].

Several implementations go to elaborate lengths to match exponent length to perceived prime strength. The Cryptlib library fits a quadratic curve to the small exponent attack cost table in the original van Oorschot paper [69] and uses the fitted curve to determine safe key lengths [41]. The Crypto++ library uses an explicit "work factor" calculation, evaluating the function  $2.4n^{1/3}(\log n)^{2/3}$  [46]. Subgroup order and exponent lengths are set to twice the calculated work factor. The work factor calculation is taken from a 1995 paper by Odlyzko on integer factorization [58]. Botan, a C++ cryptography and TLS library, uses a similar work factor calculation, derived from RFC 3766 [42], which describes best practices as of 2004 for selecting public key strengths when exchanging symmetric keys. RFC 3766 uses a similar work factor algorithm to Odlyzko, intended to model the running time of the number-field sieve. Botan then doubles the length of the work factor to obtain subgroup and exponent lengths [9].

## <span id="page-5-0"></span>D. Measurements

We used ZMap [32] to probe the public IPv4 address space for hosts serving three TLS-based protocols: HTTPS, SMTP+STARTTLS, and POP3S. To determine which primes servers were using, we sent a ClientHello message containing only ephemeral Diffie-Hellman cipher suites. We combined this data with scans from Censys [30] to determine the overall population. The results are summarized in Table III.

In August 2016, we conducted additional scans of a random 1% sample of HTTPS hosts on the Internet. First, we checked for nontrivial small subgroup attack vulnerability. For servers that sent us a prime p such that p-1 was divisible by 7, we attempted a handshake using a client key exchange value of

<span id="page-6-0"></span>

|          |           |             | Number of hosts that use |                    |                     |                                         |
|----------|-----------|-------------|--------------------------|--------------------|---------------------|-----------------------------------------|
| Protocol | Scan Date | Total Hosts | Diffie-Hellman           | Non-Safe<br>Primes | Static<br>Exponents | Static Exponents and<br>Non-Safe Primes |
| HTTPS    | 2/2016    | 40,578,754  | 10,827,565               | 1,661,856          | 964,356             | 309,891                                 |
| POP3S    | 10/2015   | 4,368,656   | 3,371,616                | 26,285             | 32,215              | 25                                      |
| STARTTLS | 10/2015   | 3,426,360   | 3,036,408                | 1,186,322          | 30,017              | 932                                     |
| SSH      | 10/2015   | 15,226,362  | 10,730,527               | 281                | 1,147               | 0                                       |
| IKEv1    | 2/2016    | 2,571,900   | 2,571,900                | 340,300            | 109                 | 0                                       |
| IKEv2    | 2/2016    | 1,265,800   | 1,265,800                | 177,000            | 52                  | 0                                       |

TABLE III: IPv4 non-safe prime and static exponent usage—Although non-safe primes see widespread use across most protocols, only a small number of hosts reuse exponents and use non-safe primes; these hosts are prime candidates for a small subgroup key recovery attack.

g<sup>7</sup> mod p, where g<sup>7</sup> is a generator of a subgroup of order 7. (7 is the smallest prime factor of p − 1 for Group 22.) When we send g7, we expect to correctly guess the PreMasterSecret and complete the handshake with one seventh of hosts that do not validate subgroup order. In our scan, we were able to successfully complete a handshake with 1477 of 10714 hosts that offered a prime such that p−1 was divisible by 7, implying that approximately 96% of these hosts fail to validate subgroup order six months after OpenSSL pushed a patch adding group order validation for correctly configured groups.

Second, we measured how many hosts performed even the most basic validation of key exchange values. We attempted to connect to HTTPS hosts with the client key exchange values of y<sup>c</sup> = 0 mod p, 1 mod p, −1 mod p. As Table [IV](#page-6-1) shows, we found that over 5% of hosts that accepted DHE ciphersuites accepted the key exchange value of −1 mod p and derived the PreMasterSecret from it. These implementations are vulnerable to a trivial version of the small subgroup confinement attacks described in Section [III-A,](#page-4-0) for *any* prime modulus p. By examining the default web pages of many of these hosts, we identified products from several notable companies including Microsoft, Cisco, and VMWare. When we disclosed these findings, VMWare notified us that they had already applied the fix in the latest version of their products; Microsoft acknowledged the missing checks but chose not to include them since they only use safe primes, and adding the checks may break functionality for some clients that were sending

<span id="page-6-1"></span>

| Key Exchange Value | Support DHE | Accepted |
|--------------------|-------------|----------|
| 0 mod p            | 143.5 K     | 87       |
| 1 mod p            | 142.2 K     | 4.9 K    |
| -1 mod p           | 143.5 K     | 7.6 K    |
| g7 mod p           | 10.7 K      | 1.5 K    |

TABLE IV: TLS key exchange validation—We performed a 1% HTTPS scan in August 2016 to check if servers validated received client key exchange values, offering generators of subgroups of order 1, 2 and 7. Our baseline DHE support number counts hosts willing to negotiate a DHE key exchange, and in the case of g7, if p−1 is divisible by 7. We count hosts as "Accepted" if they reply to the ClientKeyExchange message with a Finished message. For g7, we expect this to happen with probability 1/7, suggesting that nearly all of the hosts in our scan did not validate subgroup order.

unusual key exchange values; and Cisco informed us that they would investigate the issue.

Of 40.6 M total HTTPS hosts found in our scans, 10.8 M (27%) supported ephemeral Diffie-Hellman, of which 1.6 M (4%) used a non-safe prime, and 309 K (0.8%) used a nonsafe prime and reused exponents across multiple connections, making them likely candidates for a small subgroup key recovery attack. We note that the numbers for hosts reusing exponents are an underestimate, since we only mark hosts as such if we found them using the same public Diffie-Hellman value across multiple connections, and some load balancers that cycle among multiple values might have evaded detection.

While 77% of POP3S hosts and 39% of SMTP servers used a non-safe prime, a much smaller number used a non-safe prime and reused exponents (<0.01% in both protocols), suggesting that the popular implementations (Postfix and Dovecot [\[31\]](#page-14-34)) that use these primes follow recommendations to use ephemeral Diffie-Hellman values with DSA primes.

Table [V](#page-7-0) shows nine groups that accounted for the majority of non-safe primes used by hosts in the wild. Over 1.17 M hosts across all of our HTTPS scans negotiated Group 22 in a key exchange. To get a better picture of which implementations provide support for this group, we examined the default web pages of these hosts to identify companies and products, which we show in Table [VI.](#page-7-1)

Of the the 307 K HTTPS hosts that both use non-safe primes and reuse exponents, 277 K (90%) belong to hosts behind Amazon's Elastic Load Balancer [\[8\]](#page-13-12). These hosts use a 1024-bit prime with a 160-bit subgroup. We set up our own load balancer instance and found that the implementation failed to validate subgroup order. We were able to use a small-subgroup key recovery attack to compute 17 bits of our load balancer's private Diffie-Hellman exponent x<sup>s</sup> in only 3813 queries. We responsibly disclosed this vulnerability to Amazon. Amazon informed us that they have removed Diffie-Hellman from their recommended ELB security policy, and are encouraging customers to use the latest policy. In May 2016, we performed additional scans and found that 88% of hosts using this prime no longer repeated exponents. We give a partial factorization for p − 1 in Table [XII;](#page-13-13) the next largest subgroups have 61 and 89 bits and an offline attack against the remaining bits of a 160-bit exponent would take 2 <sup>71</sup> time. For more details on the computation, see Section [VI.](#page-11-0)

SSLeay [\[33\]](#page-14-35), a predecessor for OpenSSL, includes several default Diffie-Hellman primes, including a 512-bit prime. We found that 717 SMTP servers used a version of the

<span id="page-7-0"></span>

|                       | Group      |               |            | Host Counts |           |            |  |
|-----------------------|------------|---------------|------------|-------------|-----------|------------|--|
| Source                | Prime Size | Subgroup Size | HTTPS      | SMTP        | POP3S     | SSH        |  |
| RFC 5114 Group 22     | 1024       | 160           | 1,173,147  | 145         | 86        | 0          |  |
| Amazon Load Balancer  | 1024       | 160           | 277,858    | 0           | 1         | 0          |  |
| JDK                   | 768        | 160           | 146,491    | 671         | 16,515    | 0          |  |
| JDK                   | 1024       | 160           | 52,726     | 2,445       | 9,510     | 0          |  |
| RFC 5114 Group 24     | 2048       | 256           | 3,543      | 5           | 0         | 6          |  |
| JDK                   | 2048       | 224           | 982        | 12          | 20        | 0          |  |
| Epson Device          | 1024       | < 948         | 372        | 0           | 0         | 0          |  |
| RFC 5114 Group 23     | 2048       | 224           | 371        | 1,140,363   | 2         | 0          |  |
| Mistyped OpenSSL 512  | 512        | 497           | 0          | 717         | 0         | 0          |  |
| Other Non-Safe Primes | -          | -             | 6,366      | 41,964      | 151       | 275        |  |
| Safe Primes           | -          | -             | 9,165,709  | 1,850,086   | 3,345,331 | 10,730,246 |  |
| Total                 |            |               | 10,827,565 | 3,036,408   | 3,371,616 | 10,730,527 |  |

TABLE V: IPv4 top non-safe primes—Nine non-safe primes account for the majority of hosts using non-safe primes.

OpenSSL 512-bit prime with a single character difference in the hexadecimal representation. The resulting modulus that these servers use for their Diffie-Hellman key exchange is no longer prime. We include the factorization of this modulus along with the factors of the resulting group order in Table XII. The use of a composite modulus further decreases the work required to perform a small subgroup attack.

Although TLS also includes static Diffie-Hellman cipher suites that require a DSS certificate, we did not include them in our study; no browser supports static Diffie-Hellman [44], and Censys shows no hosts with DSS certificates, with only 652 total hosts with non-RSA or ECDSA certificates.

## IV. IPSEC

IPsec is a set of Layer-3 protocols which add confidentiality, data protection, sender authentication, and access control to IP traffic. IPsec is commonly used to implement VPNs. IPsec uses the Internet Key Exchange (IKE) protocol to determine the keys used to secure a session. IPsec may use IKEv1 [43] or IKEv2 [49]. While IKEv2 is not backwards-compatible with IKEv1, the two protocols are similar in message structure and purpose. Both versions use Diffie-Hellman to negotiate shared secrets. The groups used are limited to a fixed set of pre-determined choices, which include the DSA groups from RFC 5114, each assigned a number by IANA [49], [51], [53].

<span id="page-7-1"></span>

| Company                | Product(s)        | Count   |
|------------------------|-------------------|---------|
| Ubiquiti Networks      | airOS/EdgeOS      | 272,690 |
| Cisco                  | DPC3848VM Gateway | 65,026  |
| WatchGuard             | Fireware XTM      | 62,682  |
| Supermicro             | IPMI              | 42,973  |
| ASUS                   | AiCloud           | 39,749  |
| Electric Sheep Fencing | pfSense           | 14,218  |
| Bouygues Telecom       | Bbox              | 13,387  |
| Other                  | —                 | 135,432 |

TABLE VI: HTTPS support for RFC5114 Group 22—In a 100% HTTPS scan performed in October 2016, we found that of the 12,835,911 hosts that accepted Diffie-Hellman key exchange, 901,656 used Group 22. We were able to download default web pages for 646,157 of these hosts, which we examined to identify companies and products.

IKEv1. IKEv1 [43], [55], [60] has two basic methods for authenticated key exchange: Main Mode and Aggressive Mode. Main Mode requires six messages to establish the requisite state. The initiator sends a Security Association (SA) payload, containing a selection of cipher suites and Diffie-Hellman groups they are willing to negotiate. The responder selects a cipher and responds with its own SA payload. After the cipher suite is selected, the initiator and responder both transmit Key Exchange (KE) payloads containing public Diffie-Hellman values for the chosen group. At this point, both parties compute shared key materials, denoted SKEYID. When using signatures for authentication, SKEYID is computed SKEYID =  $\operatorname{prf}(N_i|N_r,g^{x_ix_r})$ . For the other two authentication modes, pre-shared key and public-key encryption, SKEYID is derived from the pre-shared key and session cookies, respectively, and does not depend on the negotiated Diffie-Hellman shared secret.

Each party then in turn sends an authentication message (AUTH) derived from a hash over SKEYID and the handshake. The authentication messages are encrypted and authenticated using keys derived from the Diffie-Hellman secret  $g^{x_ix_r}$ . The responder only sends her AUTH message after receiving and validating the initiator's AUTH message.

Aggressive Mode operates identically to Main Mode, but in order to reduce latency, the initiator sends SA and KE messages together, and the responder replies with its SA, KE, and AUTH messages together. In aggressive mode, the responder sends an authentication message first, and the authentication messages are not encrypted.

**IKEv2.** IKEv2 [48], [49] combines the SA and KE messages into a single message. The initiator provides a best guess ciphersuite for the KE message. If the responder accepts that proposal and chooses not to renegotiate, the responder replies with a single message containing both SA and KE payloads. Both parties then send and verify AUTH messages, starting with the initiator. The authentication messages are encrypted using session keys derived from the SKEYSEED value which is derived from the negotiated Diffie-Hellman shared secret. The standard authentication modes use public-key signatures over the handshake values.

## A. Small Subgroup Attacks in IPsec

There are several variants of small subgroup attacks against IKEv1 and IKEv2. We describe the attacks against these protocols together in this section.

Small subgroup confinement attacks. First, consider attacks that can be carried out by an attacking initiator or responder. In IKEv1 Main Mode and in IKEv2, either peer can carry out a small subgroup confinement attack against the other by sending a generator of a small subgroup as its key exchange value. The attacking peer must then guess the other peer's view of the Diffie-Hellman shared secret to compute the session keys to encrypt its authentication message, leading to a mostly online attack. However, in IKEv1 Aggressive Mode, the responder sends its AUTH message before the initiator, and this value is not encrypted with a session key. If signature authentication is being used, the SKEYID and resulting hashes are derived from the Diffie-Hellman shared secret, so the initiator can perform an offline brute-force attack against the responder's authentication message to learn their exponent in the small subgroup.

Now, consider a man-in-the-middle attacker. Bhargavan, Delignat-Lavaud, and Pironti [25] describe a transcript synchronization attack against IKEv2 that relies on a small subgroup confinement attack. A man-in-the-middle attacker initiates simultaneous connections with an initiator and a responder using identical nonces, and sends a generator  $g_i$  for a subgroup of small order  $q_i$  to each as its KE message. The two sides have a  $1/q_i$  chance of negotiating an identical shared secret, so an authentication method depending only on nonces and shared secrets could be forwarded, and the session keys would be identical.

If the attacker also has knowledge of the secrets used for authentication, more attacks are possible. Similar to the attack described for TLS, such an attacker can use a small subgroup confinement attack to force a connection to use weak encryption. The attacker only needs to rewrite a small number of handshake messages; any further encrypted communications can then be decrypted at leisure without requiring the man-in-the-middle attacker to continuously rewrite the connection. We consider a man-in-the-middle attacker who modifies the key exchange message from both the initiator and the responder to substitute a generator  $g_i$  of a subgroup of small order  $q_i$ . The attacker must then replace the handshake authentication messages, which would require knowledge of the long-term authentication secret. We describe this attack for each of pre-shared key, signatures, and public-key authentication.

For pre-shared key authentication in IKEv1 Main Mode, IKEv1 Aggressive Mode, and IKEv2, the man-in-the-middle attacker must only know the pre-shared key to construct the authentication hash; the authentication message does not depend on the negotiated Diffie-Hellman shared secret. With probability  $1/q_i$ , the two parties will agree on the Diffie-Hellman shared secret. The attacker can then brute force this value after viewing messages encrypted with keys derived from it.

For signature authentication in IKEv1 Main Mode and in IKEv2, the signed hash transmitted from each side is derived from the nonces and the negotiated shared secret, which is confined to one of  $q_i$  possible values. The attacker must know the private signing keys for both initiator and responder and brute force <code>SKEYID</code> from the received signature in order to forge the modified authentication signatures on each side. The

communicating parties will have a  $q_i$  chance of agreeing on the same value for the shared secret to allow the attack to succeed. For IKEv1 Aggressive Mode, the attack can be made to succeed every time. The responder's key exchange message is sent together with their signature which depends on the negotiated shared secret, so the man-in-the-middle attacker can brute force the  $q_i$  possible values of the responders private key  $x_r$  and replace the responder's key exchange message with  $q_i^{x_r}$ , forging an appropriate signature with their knowledge of the signing key.

For public key authentication in IKEv1 Main Mode, IKEv1 Aggressive Mode, and IKEv2, the attacker must know the private keys corresponding to the public keys used to encrypt the ID and nonce values on both sides in order to forge a valid authentication hash. Since the authentication does not depend on the shared Diffie-Hellman negotiated value, a man-in-the-middle attacker must then brute force the negotiated shared key once they receives a message encrypted with the derived key. The two parties will agree on their view of the shared key with probability  $1/q_i$ , allowing the attack to succeed.

Small subgroup key recovery attacks. Similar to TLS, an IKE responder that reuses private exponents and does not verify that the initiator key exchange values are in the correct subgroup is vulnerable to a small subgroup key recovery attack. The most recent version of the IKEv2 specification has a section discussing reuse of Diffie-Hellman exponents, and states that "because computing Diffie-Hellman exponentials is computationally expensive, an endpoint may find it advantageous to reuse those exponentials for multiple connection setups" [49]. Following this recommendation could leave a host open to a key recovery attack, depending on how exponent reuse is implemented. A small subgroup key recovery attack on IKE would be primarily offline for IKEv1 with signature authentication and for IKEv2 against the initiator.

For each subgroup of order  $q_i$ , the attacker's goal is to obtain a responder AUTH message, which depends on the secret chosen by the responder. If an AUTH message can be obtained, the attacker can brute-force the responder's secret within the subgroup offline. This is possible if the server supports IKEv1 Aggressive Mode, since the server authenticates before the client, and signature authentication produces a value dependent on the negotiated secret. In all other IKE modes, the client authenticates first, leading to an online attack. The flow of the attack is identical to TLS; for more details see Section III.

Ferguson and Schneier [34] describe a hypothetical smallsubgroup attack against the initiator where a man-in-the-middle attacker abuses undefined behavior with respect to UDP packet retransmissions. A malicious party could "retransmit" many key exchange messages to an initiator and potentially receive a different authentication message in response to each, allowing a mostly offline key recovery attack.

## B. Implementations

We examined several open-source IKE implementations to understand server behavior. In particular, we looked for implementations that generate small Diffie-Hellman exponents, repeat exponents across multiple connections, or do not correctly validate subgroup order. Despite the suggestion in IKEv2 RFC 7296 to reuse exponents [49], none of the implementations that we examined reused secret exponents.

All implementations we reviewed are based on

FreeS/WAN [\[13\]](#page-13-14), a reference implementation of IPSec. The final release of FreeS/Wan, version 2.06, was released in 2004. Version 2.04 was forked into Openswan [\[16\]](#page-13-15) and strongSwan [\[17\]](#page-13-16), with a further fork of Openswan into Libreswan [\[14\]](#page-13-17) in 2012. The final release of FreeS/WAN used constant length 256-bit exponents but did not support RFC 5114 DSA groups, offering only the Oakley 1024-bit and 1536-bit groups that use safe primes.

Openswan does not generate keys with short exponents. By default, RFC 5114 groups are not supported, although there is a compile-time option that can be explicitly set to enable support for DSA groups. strongSwan both supports RFC 5114 groups and has explicit hard-coded exponent sizes for each group. The exponent size for each of the RFC 5114 DSA groups matches the subgroup size. However, these exponent sizes are only used if the dh\_exponent\_ansi\_x9\_42 configuration option is set. It also includes a routine inside an #ifdef that validates subgroup order by checking that g <sup>q</sup> ≡ 1 mod p, but validation is not enabled by default. Libreswan uses Mozilla Network Security Services (NSS) [\[7\]](#page-13-8) to generate Diffie-Hellman keys. As discussed in Section [III-C,](#page-5-2) NSS generates short exponents for Diffie-Hellman groups. Libreswan was forked from Openswan after support for RFC 5114 was added, and retains support for those groups if it is configured to use them.

Although none of the implementations we examined were configured to reuse Diffie-Hellman exponents across connections, the failure to validate subgroup orders even for the prespecified groups renders these implementations fragile to future changes and vulnerable to subgroup confinement attacks.

Several closed source implementations also provide support for RFC 5114 Group 24. These include Cisco's IOS [\[27\]](#page-14-41), Juniper's Junos [\[47\]](#page-14-42), and Windows Server 2012 R2 [\[56\]](#page-14-43). We were unable to examine the source code for these implementations to determine whether or not they validate subgroup order.

## *C. Measurements*

We performed a series of Internet scans using ZMap to identify IKE responders. In our analysis, we only consider hosts that respond to our ZMap scan probes. Many IKE hosts that filter their connections based on IP are excluded from our results. We further note that, depending on VPN server configurations, some responders may continue with a negotiation that uses weak parameters until they are able to identify a configuration for the connecting initiator. At that point, they might reject the connection. As an unauthenticated initiator, we have no way of distinguishing this behavior from the behaviour of a VPN server that legitimately accepts weak parameters. For a more detailed explanation of possible IKE responder behaviors in response to scanning probes, see Wouters [\[70\]](#page-14-44).

In October 2016, we performed a series of scans offering the most common cipher suites and group parameters we found in implementations to establish a baseline population for IKEv1 and IKEv2 responses. For IKEv1, the baseline scan offered Oakley groups 2 and 14 and RFC 5114 groups 22, 23, and 24 for the group parameters; SHA1 or SHA256 for the hash function; pre-shared key or RSA signatures for the authentication method; and AES-CBC, 3DES, and DES for the encryption algorithm. Our IKEv2 baseline scan was similar, but also offered the 256 bit and 384-bit ECP groups and AES-GCM for authenticated encryption.

On top of the baseline scans, we performed additional scans

to measure support for the non-safe RFC 5114 groups and for key exchange parameter validation. Table [VII](#page-10-0) shows the results of the October IKE scans. For each RFC 5114 DSA group, we performed four handshakes with each host; the first tested for support by sending a valid client key exchange value, and the three others tested values that should be rejected by a properlyvalidating host. We did not scan using the key exchange value 0 because of a vulnerability present in unpatched Libreswan and Openswan implementations that causes the IKE daemon to restart when it receives such a value [\[3\]](#page-13-18).

We considered a host to accept our key exchange value if after receiving the value, it continued the handshake without any indication of an error. We found that 33.2% of IKEv1 hosts and 17.7% of IKEv2 hosts that responded to our baseline scans supported using one of the RFC 5114 groups, and that a surprising number of hosts failed to validate key exchange values. 24.8% of IKEv1 hosts that accepted Group 23 with a valid key exchange value also accepted 1 mod p or −1 mod p as a key exchange value, even though this is explicitly warned against in the RFC [\[59\]](#page-14-12). This behavior leaves these hosts open to a small subgroup confinement attack even for safe primes, as described in Section [II-F.](#page-2-0)

For safe groups, a check that the key exchange value is strictly between 1 and p − 1 is sufficient validation. However, when using non-safe DSA primes, it is also necessary to verify that the key exchange value lies within the correct subgroup (i.e., y <sup>q</sup> ≡ 1 mod p). To test this case, we constructed a generator of a subgroup that was not the intended DSA subgroup, and offered that as our key exchange value. We did not find any IKEv1 hosts that rejected this key exchange value after previously accepting a valid key exchange value for the given group. For IKEv2, the results were similar with the exception of Group 24, where still over 93% of hosts accepted this key exchange value. This suggests that almost no hosts supporting DSA groups are correctly validating subgroup order.

We observed that across all of the IKE scans, 109 IKEv1 hosts and 52 IKEv2 hosts repeated a key exchange value. This may be due to entropy issues in key generation rather than static Diffie-Hellman exponents; we also found 15,891 repeated key exchange values across different IP addresses. We found no hosts that used both repeated key exchange values and non-safe groups. We summarize these results in Table [III.](#page-6-0)

# V. SSH

SSH contains three key agreement methods that make use of Diffie-Hellman. The "Group 1" and "Group 14" methods denote Oakley Group 2 and Oakley Group 14, respectively [\[71\]](#page-14-15). Both of these groups use safe primes. The third method, "Group Exchange", allows server to select a custom group [\[35\]](#page-14-45). The group exchange RFC specifies that all custom groups should use safe primes. Despite this, RFC 5114 notes that group exchange method allows for its DSA groups in SSH, and advocates for their immediate inclusion [\[53\]](#page-14-3).

In all Diffie-Hellman key agreement methods, after negotiating cipher selection and group parameters, the SSH client generates a public key exchange value y<sup>c</sup> = g <sup>x</sup><sup>c</sup> mod p and sends it to the server. The server computes its own Diffie-Hellman public value y<sup>s</sup> = g <sup>x</sup><sup>s</sup> mod p and sends it to the client, along with a signature from its host key over the resulting shared secret Y = g <sup>x</sup>sx<sup>c</sup> mod p and the hash of the handshake so far. The client verifies the signature before continuing.

<span id="page-10-0"></span>

|          |                                             |          |             | Client key exchange public values offered... |               |  |
|----------|---------------------------------------------|----------|-------------|----------------------------------------------|---------------|--|
| Protocol | Groups Offered                              | Support  | $1 \bmod p$ | $-1 \bmod p$                                 | $g_s \bmod p$ |  |
| IKEv1    | Group 22                                    | 332.4 K  | 82.6 K      | 78.5 K                                       | 332.4 K       |  |
|          | Group 23                                    | 333.4 K  | 82.5 K      | 82.5 K                                       | 333.4 K       |  |
|          | Group 24                                    | 379.8 K  | 93.9 K      | 95.2 K                                       | 379.8 K       |  |
|          | Baseline (Groups 2, 14, 22, 23, 24)         | 1139.3 K | -           | -                                            | -             |  |
| IKEv2    | Group 22                                    | 182.1 K  | 553         | 553                                          | 181.9 K       |  |
|          | Group 23                                    | 181.9 K  | 542         | 550                                          | 180.1 K       |  |
|          | Group 24                                    | 213.0 K  | 2245        | 2173                                         | 200.0 K       |  |
|          | Baseline (Groups 2, 14, 19, 20, 22, 23, 24) | 1203.7 K | -           | -                                            | -             |  |

TABLE VII: **IKE group support and validation.**—We measured support for RFC5114 DSA groups in IKEv1 and IKEv2 and test for key exchange validation by performing a series of 100% IPv4 scans in October 2016. For Group 23,  $g_s$  is a generator of a subgroup with order 3, and for Groups 22 and 24,  $g_s$  is a generator of a subgroup of order 7.

## A. Small Subgroup Attacks in SSH

Small subgroup confinement attacks. An SSH client could execute a small subgroup confinement attack against an SSH server by sending a generator  $g_i$  for a subgroup of small order  $q_i$  as its client key exchange, and immediately receive the server's key exchange  $g^{x_s} \mod p$  together with a signature that depends on the server's view of the shared secret  $Y_s = g_i^{x_s} \mod p$ . For small  $q_i$ , this allows the client to brute force the value of  $x_s \mod q_i$  offline and compare to the server's signed handshake to learn the correct value of  $x_s \mod q_i$ . To avoid this, the SSH RFC specifically recommends using safe primes, and to use exponents at least twice the length of key material derived from the shared secret [35].

If client and server support Diffie-Hellman group exchange and the server uses a non-safe prime, a man in the middle with knowledge of the server's long-term private signing key can use a small subgroup confinement attack to man-in-the-middle the connection without having to rewrite every message. The attack is similar to the case of TLS: the man in the middle modifies the server group and key exchange messages, leaving the prime unchanged, but substituting a generator  $g_i$  of a subgroup of small order  $q_i$  for the group generator and  $g_i$  for the server's key exchange value  $y_s$ . The client then responds with a client key exchange message  $y_c = g_i^{x_c} \mod p$ , which the man in the middle leaves unchanged. The attacker then forges a correct signature for the modified server group and key exchange messages and passes it to the client. The server's view of the shared secret is  $g_i^{x_c x_s} \mod p$ , and the client's view of the shared secret is  $g_i^{x_c} \mod p$ . As in the attack described for TLS, these views are identical when  $x_s \equiv 1 \mod q_i$ , so this connection will succeed with probability  $1/q_i$ . For a small enough  $q_i$ , this enables a man in the middle to use a compromised server signing key to decrypt traffic with a reasonable probability of success, while only requiring tampering with the initial handshake messages, rather than having to actively rewrite the entire connection for the duration of the session.

**Small subgroup key recovery attacks.** Since the server immediately sends a signature over the public values and the Diffie-Hellman shared secret, an implementation using static exponents and non-safe primes that is vulnerable to a small subgroup confinement attack would also be vulnerable to a mostly offline key recovery attack, as a malicious client would only need to send a single key exchange message per subgroup.

## B. Implementations

Censys [30] SSH banner scans show that the two most common SSH server implementations are Dropbear and OpenSSH. Dropbear group exchange uses hard-coded safe prime parameters from the Oakley groups and validates that client key exchange values are greater than 1 and less than p-1. While OpenSSH only includes safe primes by default, it does provide the ability to add additional primes and does not provide the ability to specify subgroup orders. Both OpenSSH and Dropbear generate fresh exponents per connection.

We find one SSH implementation, Cerberus SFTP server (FTP over SSH), repeating server exponents across connections. Cerberus uses OpenSSL, but fails to set SSL\_OP\_SINGLE-\_DH\_USE, which was required to avoid exponent reuse prior to OpenSSL 1.0.2f.

## C. Measurements

Of the 15.2 M SSH servers on Censys, of which 10.7 M support Diffie-Hellman group exchange, we found that 281 used a non-safe prime, and that 1.1 K reused Diffie-Hellman exponents. All but 26 of the hosts that reused exponents had banners identifying the Cerberus SFTP server. We encountered no servers that both reused exponents and used non-safe primes.

We performed a scan of 1% of SSH hosts in February 2016 offering the key exchange values of  $y_c = 0 \mod p$ ,  $1 \mod p$  and  $p-1 \mod p$ . As Table VIII shows, 33% of SSH hosts failed to validate group order when we sent the key exchange value  $p-1 \mod p$ . Even when safe groups are used, this behaviour allows an attacker to learn a single bit of the private exponent, violating the decisional Diffie-Hellman assumption and leaving the implementation open to a small subgroup confinement

<span id="page-10-1"></span>

| Key Exchange Value | Handshake Initiated | Accepted |
|--------------------|---------------------|----------|
| $0 \bmod p$        | 175.6 K             | 5.7 K    |
| $1 \bmod p$        | 175.0 K             | 43.9 K   |
| $-1 \bmod p$       | 176.0 K             | 59.0 K   |

TABLE VIII: **SSH validation**—In a 1% SSH scan performed in February 2016, we sent the key exchange values  $y_c = 0, 1$  and p-1. We count hosts as having initiated a handshake if they send a SSH\_MSG\_KEX\_DH\_GEX\_GROUP, and we count hosts as "Accepted" if they reply to the client key exchange message with a SSH\_MSG\_KEX\_DH\_GEX\_REPLY.

<span id="page-11-1"></span>

| Prime | lg(p) | Exact Order Known |          |          |          |             | Exact Order Unknown |              |              |            |
|-------|-------|-------------------|----------|----------|----------|-------------|---------------------|--------------|--------------|------------|
|       |       | 160 bits          | 224 bits | 256 bits | 300 bits | $lg(p) - 8$ | $lg(p) - 32$        | $lg(p) - 64$ | Unlikely DSA | Likely DSA |
| 512   |       | 3                 | 0        | 0        | 0        | 5           | 0                   | 0            | 760          | 43         |
| 768   |       | 4                 | 0        | 0        | 4        | 2,685       | 0                   | 0            | 220          | 1,402      |
| 1024  |       | 29                | 0        | 0        | 0        | 323         | 944                 | 176          | 1,559        | 26,881     |
| 2048  |       | 0                 | 1        | 1        | 0        | 0           | 0                   | 0            | 1,128        | 4,890      |
| 3072  |       | 0                 | 0        | 0        | 0        | 0           | 5                   | 0            | 9            | 152        |
| 4096  |       | 4                 | 0        | 0        | 0        | 0           | 0                   | 0            | 20           | 183        |
| 8192  |       | 0                 | 0        | 0        | 0        | 0           | 0                   | 0            | 0            | 1          |
| Other |       | 0                 | 0        | 0        | 0        | 0           | 0                   | 0            | 400          | 15         |

TABLE IX: **Distribution of orders for groups with non-safe primes**—For groups for which we were able to determine the subgroup order exactly, 160-bits subgroup orders are common. We classify other groups to be likely DSA groups if we know that the subgroup order is at least 8 bits smaller than the prime.

attack (Section III-A).

<span id="page-11-0"></span>

## VI. FACTORING GROUP ORDERS OF NON-SAFE PRIMES

Across all scans, we collected 41,847 unique groups with non-safe primes. To measure the extent to which each group would facilitate a small subgroup attack in a vulnerable implementation, we attempted to factor (p-1)/2. We used the GMP-ECM [39] implementation of the elliptic curve method for integer factorization on a local cluster with 288 cores over a several-week period to opportunistically find small factors of the group order for each of the primes.

Given a group with prime p and a generator g, we can check whether the generator generates the entire group or generates a subgroup by testing whether  $g^{q_i} \equiv 1 \mod p$  for each factor  $q_i$  of (p-1)/2. When  $g^{q_i} \equiv 1 \mod p$ , then if  $q_i$  is prime, we know that  $q_i$  is the exact order of the subgroup generated by g; otherwise  $q_i$  is a multiple of the order of the subgroup. We show the distribution of group order for groups using non-safe primes in Table IX. We were able to completely factor p-1 for 4,701 primes. For the remaining primes, we did not obtain enough factors of (p-1)/2 to determine the group order.

Of the groups where we were able to deduce the exact subgroup orders, several thousand had a generator for a subgroup that was either 8, 32, or 64 bits shorter than the prime itself. Most of these were generated by the Xlight FTP server, a closed-source implementation supporting SFTP. It is not clear whether this behavior is intentional or a bug in an implementation intending to generate safe primes. Primes of this form would lead to a more limited subgroup confinement or key recovery attack.

Given the factorization of (p-1)/2, and a limit for the amount of online and offline work an attacker is willing to invest, we can estimate the vulnerability of a given group to a hypothetical small subgroup key recovery attack. For each subgroup of order  $q_i$ , where  $q_i$  is less than the online work limit, we can learn  $q_i$  bits of the secret key via an online brute-force attack over all elements of the subgroup. To recover the remaining bits of the secret key, an attacker could use the Pollard lambda algorithm, which runs in time proportional to the square root of the remaining search space. If this runtime is less than the offline work limit, we can recover the entire secret key. We give work estimates for the primes we were able to factor and the number of hosts that would be affected by such a hypothetical attack in Table X.

The DSA groups introduced in RFC 5114 [53] are of

particular interest. We were able to completely factor (p-1)/2 for both Group 22 and Group 24, and found several factors for Group 23. We give these factorizations in Table XII. In Table XI, we show the amount of online and offline work required to recover a secret exponent for each of the RFC 5114 groups. In particular, an exponent of the recommended size used with Group 23 is fully recoverable via a small subgroup attack with 33 bits of online work and 47 bits of offline work.

## VII. DISCUSSION

The small subgroup attacks require a number of special conditions to go wrong in order to be feasible. For the case of small subgroup confinement attacks, a server must both use a non-safe group and fail to validate subgroup order; the widespread failure of implementations to implement or enable group order validation means that large numbers of hosts using non-"safe" primes are vulnerable to this type of attack.

For a full key recovery attack to be possible the server must additionally reuse a small static exponent. In one sense, it is surprising that any implementations might satisfy all of the requirements for a full key recovery attack at once. However, when considering all of the choices that cryptographic libraries leave to application developers when using Diffie-Hellman, it is surprising that any protocol implementations manage to use Diffie-Hellman securely at all.

We now use our results to draw lessons for the security and cryptographic communities, provide recommendations for future cryptographic protocols, and suggest further research.

RFC 5114 Design Rationale. Neither NIST SP 800-56A nor RFC 5114 give a technical justification for fixing a much smaller subgroup order than the prime size. Using a shorter private exponent comes with performance benefits. However, there are no known attacks that would render a short exponent used with a safe prime less secure than an equivalently-sized exponent used with in a subgroup with order matched to the exponent length. The cryptanalyses of both short exponents and small subgroups are decades old.

If anything, the need to perform an additional modular exponentiation to validate subgroup order makes Diffie-Hellman over DSA groups *more* expensive than the safe prime case, for identical exponent lengths. As a more minor effect, a number field sieve-based cryptanalytic attack against a DSA prime is computationally slightly easier than against a safe prime. The design rationale may have its roots in preferring to implicitly use the assumption that Diffie-Hellman is secure for a small

<span id="page-12-0"></span>

|          | Work (bits) |         | HTTPS  |       | MAIL   |           | SSH    |       |
|----------|-------------|---------|--------|-------|--------|-----------|--------|-------|
| Exponent | Online      | Offline | Groups | Hosts | Groups | Hosts     | Groups | Hosts |
| 160      | 20          | 30      | 3      | 2     | 3      | 7         | 0      | 0     |
| 160      | 30          | 45      | 517    | 1,996 | 1963   | 1,143,524 | 11     | 10    |
| 160      | 40          | 60      | 3,701  | 8,495 | 13,547 | 1,159,853 | 109    | 68    |
| 224      | 20          | 30      | 0      | 0     | 0      | 0         | 0      | 0     |
| 224      | 30          | 45      | 2      | 2     | 14     | 16        | 0      | 0     |
| 224      | 40          | 60      | 307    | 691   | 1039   | 1,141,840 | 3      | 1     |
| 256      | 20          | 30      | 0      | 0     | 0      | 0         | 0      | 0     |
| 256      | 30          | 45      | 0      | 0     | 1      | 1         | 0      | 0     |
| 256      | 40          | 60      | 42     | 478   | 180    | 1,140,668 | 0      | 0     |

TABLE X: Full key recovery attack complexity—We estimate the amount of work required to carry out a small subgroup key recovery attack, and show the prevalence of those groups in the wild. Hosts are vulnerable if they reuse exponents and fail to check subgroup order.

prime-order subgroup without conditions on exponent length, rather than assuming Diffie-Hellman with short exponents is secure inside a group of much larger order. Alternatively, this insistence may stem from the fact that the security of DSA digital signatures requires the secret exponent to be uniformly random, although no such analogous attacks are known for Diffie-Hellman key exchange. [\[57\]](#page-14-47) Unfortunately, our empirical results show that the necessity to specify and validate subgroup order for Diffie-Hellman key exchange makes implementations more fragile in practice.

Cryptographic API design. Most cryptographic libraries are designed with a large number of potential options and knobs to be tuned, leaving too many security-critical choices to the developers, who may struggle to remain current with the diverse and ever-increasing array of cryptographic attacks. These exposed knobs are likely due to a prioritization of performance over security. These confusing options in cryptographic implementations are not confined to primitive design: Georgiev et al. [\[37\]](#page-14-48) discovered that SSL certificate validation was broken in a large number of non-browser TLS applications due to developers misunderstanding and misusing library calls. In the case of the small subgroup attacks, activating most of the conditions required for the attack will provide slight performance gains for an application: using a small exponent decreases the work required for exponentiation, reusing Diffie-Hellman exponents saves time in key generation, and failing to validate subgroup order saves another exponentiation. It is not reasonable to assume that applications developers have enough understanding of algebraic groups to be able to make the appropriate choices to optimize performance while still providing sufficient security for their implementation.

<span id="page-12-1"></span>

| Group    | Exponent Size | Online Work | Offline Work |
|----------|---------------|-------------|--------------|
| Group 22 | 160           | 8           | 72           |
| Group 23 | 224           | 33          | 47           |
| Group 24 | 256           | 32          | 94           |

TABLE XI: Attacking RFC 5114 groups—We show the log of the amount of work in bits required to perform a small subgroup key recovery attack against a server that both uses a static Diffie-Hellman exponent of the same size as the subgroup order and fails to check group order.

Cryptographic standards. Cryptographic recommendations from standards committees are often too weak or vague, and, if strayed from, provide little recourse. The purpose of standardized groups and standardized validation procedures is to help remove the onus from application developers to know and understand the details of the cryptographic attacks. A developer should not have to understand the inner workings of Pollard lambda and the number field sieve in order to size an exponent; this should be clearly and unambiguously defined in a standard. However, the tangle of RFCs and standards attempting to define current best practices in key generation and parameter sizing do not paint a clear picture, and instead describe complex combinations of approaches and parameters, exposing the fragility of the cryptographic ecosystem. As a result, developers often forget or ignore edge cases, leaving many implementations of Diffie-Hellman too close to vulnerable for comfort. Rather than provide the bare minimums for security, the cryptographic recommendations from standards bodies should be designed for defense-in-depth such that a single mistake on the part of a developer does not have disastrous consequences for security. The principle of defense-in-depth has been a staple of the systems security community; cryptographic standards should similarly be designed to avoid fragility.

Protocol design. The interactions between cryptographic primitives and the needs of protocol designs can be complex. The after-the-fact introduction of RFC 5114 primes illustrates some of the unexpected difficulties: both IKE and SSH specified group validation only for safe primes, and a further RFC specifying extra group validation checks needed to be defined for IKE. Designing protocols to encompass many unnecessary functions, options, and extensions leaves room for implementation errors and makes security analysis burdensome. IKE is a notorious example of a difficult-to-implement protocol with many edge cases. Just Fast Keying (JFK), a protocol created as a successor to IKEv1, was designed to be an exceedingly simple key exchange protocol without the unnecessarily complicated negotiations present in IKE [\[19\]](#page-13-19). However, the IETF instead standardized IKEv2, which is nearly as complicated as IKEv1. Protocols and cryptosystems should be designed with the developer in mind— easy to implement and verify, with limited edge cases. The worst possible outcome is a system that appears to work, but provides less security than expected.

To construct such cryptosystems, secure-by-default primitives are key. As we show in this paper, finite-field based

<span id="page-13-13"></span>

| Source                                  | Factored Completely? | Order Factorization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RFC 5114 Group 22                       | Yes                  | 23 * 7 * df * 183a872bdc5f7a7e88170937189 * 228c5a311384c02e1f287c6b7b2d * 5a8<br>7d66c65a60728c353e32ece8be1 * f518aa8781a8df278aba4e7d64b7cb9d49462353 * 1a3adf<br>d6a69682661ca6e590b447e66ebd1bbdeab5e6f3744f06f46cf2a8300622ed50011479f18143d47<br>a53d30113995663a447dcb8e81bc24d988edc41f21                                                                                                                                                                                                                                                                                            |
| RFC 5114 Group 23                       | No                   | 32 * 5 * 2b * 49 * 9d * 5e9a5 * 93ee1 * 2c3f0539 * 136c58359 * 1a30b7358d * 33<br>a378eb0d * 801c0d34c58d93fe997177101f80535a4738cebcbf389a99b36371eb * 22bbe4b57<br>f6fc6dc24fef3f56e1c216523b3210d27b6c078b32b842aa48d35f230324e48f6dc2a10dd23d28d<br>82843a78f264495542be4a95cb05e41f80b013f8b0e3ea26b84cd497b43cc932638530a068ecc44<br>f8ea3cc84139f0667100d426b60b9ab82b8de865b0cbd633f41366622011006632e0832e827febb<br>066efe4ab4f1b2e99d96adfaf1721447b167cb49c372efcb82923b3731433cecb7ec3ebbc8d67ef<br>41b5d11fb3328851084f74de823b5402f6b038172348a147b1ceac47722e31a72fe68b44ef4b |
| RFC 5114 Group 24                       | Yes                  | 7 * d * 9f5 * 22acf * bd9f34b1 * 8cf83642a709a097b447997640129da299b1a47d1eb375<br>ba308b0fe64f5fbd3 * 15adfe949ebb242e5cd0978fac1b43fdbd2e5b0c5f48924fbbd370195c0<br>b20596d98ad0a9e3fd98876413d926f41a8b918d2ec4b018a30efe5e336bf3c7ce60d515cf46af5<br>acf3bb389f68ad0c4ed2f0b1dbb970293741eb6509c64e731802259a639a7f57d4a9c0d9445241f<br>bcdbdc50555b76d9c335c1fa4e11a8351f1bf4730dd67ffed877cc13e8ea40c7d51441c1f4e5915<br>ef1159eca75a2359f5e0284cd7f3b982c32e5c51dbf51b45f4603ef46bae528739315ca679703c1<br>fcf3b44fe3da5999daadf5606eb828fc57e46561be8c6a866361                        |
| Amazon Load<br>Balancer                 | No                   | 2 * 3 * 5 * edb * 181ac5dbfe5ce13b * 18aa349859e9e9de09b7d65 * 9414a18a7b575e8f<br>2f6cb2dbc22eb1fc21d4929 * 2de9f1171a2493d46a31d508b63532cdf86d21db6f50f717736fc<br>b0b722856a504ed4916e0484fe4ba5f5f4a9fff28a1233b728b3d043aec37c4f138ffd58fe7a8c3<br>1e93cb52be527395e45db487b61daadded9c8ec35                                                                                                                                                                                                                                                                                            |
| Mistyped OpenSSL<br>512 "Prime" Factors | Yes                  | 5 * b * a9b461e1636f4b51ef * 1851583cf5f9f731364e4aa6cdc2cac4f01* 3f0b39cacfc08<br>df4baf46c7fa7d1f4dfe184f9d22848325a91c519f79023a4526d8369e86b                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mistyped OpenSSL<br>512 Order Factors   | Yes                  | 213 * 33 * 52 * 112 * 269 * 295 * 4d5 * 97c3 * 9acfe7 * 8cdd0e128f * 385<br>b564eecd613536818f949 * 146d410923e999f8c291048dc6feffcebf8b9e99eec9a4d585f8742<br>e49b393256c23c9                                                                                                                                                                                                                                                                                                                                                                                                                |

TABLE XII: Group order factorization for common non-safe primes—We used the elliptic curve method to factor (p-1)/2 for each of the non-safe primes we found while scanning, as well as the mistyped OpenSSL "prime".

Diffie-Hellman has many edge cases that make its correct use difficult, and which occasionally arise as bugs at the protocol level. For example, SSH and TLS allow the server to generate arbitrary group parameters and send them to the client, but provide no mechanism for the server to specify the group order so that the client can validate the parameters. Diffie-Hellman key exchange over groups with different properties cannot be treated as a black-box primitive at the protocol level.

**Recommendations.** As a concrete recommendation, modern Diffie-Hellman implementations should prefer elliptic curve groups over safe curves with proper point validation [24]. These groups are much more efficient and have shorter key sizes than finite-field Diffie-Hellman at equivalent security levels. The TLS 1.3 draft includes a list of named curves designed to modern security standards [65]. If elliptic curve Diffie-Hellman is not an option, then implementations should follow the guidelines outlined in RFC 7919 for selecting finite field Diffie-Hellman primes [38]. Specifically, implementations should prefer "safe" primes of documented provenance of at least 2048 bits, validate that key exchange values are strictly between 1 and p-1, use ephemeral key exchange values for every connection, and use exponents of at least 224 bits.

## ACKNOWLEDGMENTS

We would like to thank the exceptional sysadmin Jose Antonio Insua Fernandez for his support. This material is based upon work supported by the U.S. National Science Foundation under Grants No. CNS-1345254, CNS-1408734, CNS-1409505, CNS-1505799, CNS-1513671, and CNS-1518888, an Alfred P. Sloan Foundation Research Fellowship, and a gift from Cisco.

## REFERENCES

<span id="page-13-4"></span>[1] Finite field cryptography based samples. http://csrc.nist.gov/groups/ST/toolkit/documents/Examples/KS\_FFC\_All.pdf.

- <span id="page-13-9"></span>[2] NSS dh.c. https://hg.mozilla.org/projects/nss/file/tip/lib/freebl/dh.c.
- <span id="page-13-18"></span>[3] CVE-2015-3240. Available from MITRE, CVE-ID CVE-2015-3240., Aug. 2015. http://cve.mitre.org/cgi-bin/cvename.cgi?name=2015-3240.
- <span id="page-13-7"></span>[4] Exim Internet mailer, July 2015. http://www.exim.org/.
- <span id="page-13-10"></span>[5] Mozilla bug tracker, Nov. 2015. https://bugzilla.mozilla.org/show\_bug.cgi?id=1160139.
- <span id="page-13-5"></span>[6] OpenSSL changes, Jan. 2015. https://www.openssl.org/news/cl102.txt.
- <span id="page-13-8"></span>[7] Overview of NSS, Sept. 2015. https://developer.mozilla.org/en-US/docs/ Mozilla/Projects/NSS/Overview.
- <span id="page-13-12"></span>[8] Amazon Elastic Load Balancer, 2016. https://aws.amazon.com/ elasticloadbalancing/.
- <span id="page-13-11"></span>[9] Botan, 2016. https://github.com/randombit/botan.
- <span id="page-13-1"></span>[10] Bug 1837 - small subgroup attack, May 2016. https://bugs.exim.org/ show\_bug.cgi?id=1837.
- <span id="page-13-0"></span>[11] CVE-2016-0701. Available from MITRE, CVE-ID CVE-2016-0701., Jan. 2016. http://cve.mitre.org/cgi-bin/cvename.cgi?name=2016-0701.
- <span id="page-13-2"></span>[12] Exim TLS Security, DH and standard parameters, Oct. 2016. https://lists.exim.org/lurker/message/20161008.231103.c70b2da8.en.html.
- <span id="page-13-14"></span>[13] FreeS/WAN, 2016. http://www.freeswan.org/.
- <span id="page-13-17"></span>[14] Libreswan, 2016. https://libreswan.org/.
- <span id="page-13-6"></span>[15] OpenSSL security advisory [28th Jan 2016], Jan. 2016. https://www.openssl.org/news/secadv/20160128.txt.
- <span id="page-13-15"></span>[16] Openswan, 2016. https://www.openswan.org/.
- <span id="page-13-16"></span>[17] strongSwan, 2016. https://www.strongswan.org/.
- <span id="page-13-3"></span>[18] D. Adrian, K. Bhargavan, Z. Durumeric, P. Gaudry, M. Green, J. A. Halderman, N. Heninger, D. Springall, E. Thomé, L. Valenta, B. Vander-Sloot, E. Wustrow, S. Zanella-Béguelin, and P. Zimmermann. Imperfect forward secrecy: How Diffie-Hellman fails in practice. In 22nd ACM Conference on Computer and Communications Security, Oct. 2015.
- <span id="page-13-19"></span>[19] W. Aiello, S. M. Bellovin, M. Blaze, R. Canetti, J. Ioannidis, A. D. Keromytis, and O. Reingold. Just fast keying: Key agreement in a hostile internet. ACM Transactions on Information and System Security (TISSEC), 7(2):242–273, 2004.

- <span id="page-14-18"></span>[20] R. Anderson and S. Vaudenay. Minding your p's and q's. In *ASIACRYPT*, 1996.
- <span id="page-14-11"></span>[21] E. Barker. NIST special publication 800-57 part 1 revision 4, Jan. 2014. [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r4.pdf) [57pt1r4.pdf.](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r4.pdf)
- <span id="page-14-27"></span>[22] E. Barker, W. Barker, W. Burr, W. Polk, and M. Smid. NIST special publication 800-57 part 1 (revised), Jan. 2007. [http://csrc.nist.gov/publications/](http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf) [nistpubs/800-57/sp800-57-Part1-revised2\\_Mar08-2007.pdf.](http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf)
- <span id="page-14-2"></span>[23] E. B. Barker, D. Johnson, and M. E. Smid. Sp 800-56a. recommendation for pair-wise key establishment schemes using discrete logarithm cryptography (revised). 2007.
- <span id="page-14-49"></span>[24] D. J. Bernstein and T. Lange. SafeCurves: choosing safe curves for elliptic-curve cryptography, Jan. 2014. [https://safecurves.cr.yp.to/.](https://safecurves.cr.yp.to/)
- <span id="page-14-19"></span>[25] K. Bhargavan, A. Delignat-Lavaud, and A. Pironti. Verified contributive channel bindings for compound authentication. In *Network and Distributed System Security Symposium*, 2015.
- <span id="page-14-20"></span>[26] K. Bhargavan and G. Leurent. Transcript collision attacks: Breaking authentication in TLS, IKE, and SSH. In *Network and Distributed System Security Symposium*, 2016.
- <span id="page-14-41"></span>[27] Cisco. Security for VPNs with IPsec configuration guide, 2016. [http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec\\_conn\\_](http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_vpnips/configuration/xe-3s/sec-sec-for-vpns-w-ipsec-xe-3s-book.html) [vpnips/configuration/xe-3s/sec-sec-for-vpns-w-ipsec-xe-3s-book.html.](http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_vpnips/configuration/xe-3s/sec-sec-for-vpns-w-ipsec-xe-3s-book.html)
- <span id="page-14-22"></span>[28] T. Dierks and E. Rescorla. The Transport Layer Security (TLS) protocol. IETF RFC RFC5246, 2008.
- <span id="page-14-5"></span>[29] W. Diffie and M. E. Hellman. New directions in cryptography. *IEEE Transactions on Information Theory*, 22(6):644–654, 1976.
- <span id="page-14-33"></span>[30] Z. Durumeric, D. Adrian, A. Mirian, M. Bailey, and J. A. Halderman. A search engine backed by Internet-wide scanning. In *22nd ACM Conference on Computer and Communications Security*, Oct. 2015.
- <span id="page-14-34"></span>[31] Z. Durumeric, D. Adrian, A. Mirian, J. Kasten, K. Thomas, V. Eranti, N. Lidzborski, E. Bursztein, M. Bailey, and J. A. Halderman. The Matter of Heartbleed. In *15th ACM Internet Measurement Conference*, Oct. 2015.
- <span id="page-14-32"></span>[32] Z. Durumeric, E. Wustrow, and J. A. Halderman. ZMap: Fast Internetwide scanning and its security applications. In *22nd USENIX Security Symposium*, Aug. 2013.
- <span id="page-14-35"></span>[33] Y. Eric. SSLeay, 1995. [ftp://ftp.pl.vim.org/vol/rzm1/replay.old/libraries/](ftp://ftp.pl.vim.org/vol/rzm1/replay.old/libraries/SSL.eay/SSLeay-0.5.1a.tar.gz) [SSL.eay/SSLeay-0.5.1a.tar.gz.](ftp://ftp.pl.vim.org/vol/rzm1/replay.old/libraries/SSL.eay/SSLeay-0.5.1a.tar.gz)
- <span id="page-14-40"></span>[34] N. Ferguson and B. Schneier. A cryptographic evaluation of IPsec. *Counterpane Internet Security, Inc*, 3031, 2000.
- <span id="page-14-45"></span>[35] M. Friedl, N. Provos, and W. Simpson. Diffie-Hellman group exchange for the Secure Shell (SSH) transport layer protocol. IETF RFC 4419, 2006.
- <span id="page-14-26"></span>[36] S. Gallagher. Google dumps plans for OpenSSL in Chrome, takes own Boring road, July 2014. [http://arstechnica.com/information-technology/](http://arstechnica.com/information-technology/2014/07/google-dumps-plans-for-openssl-in-chrome-takes-own-boring-road/) [2014/07/google-dumps-plans-for-openssl-in-chrome-takes-own](http://arstechnica.com/information-technology/2014/07/google-dumps-plans-for-openssl-in-chrome-takes-own-boring-road/)[boring-road/.](http://arstechnica.com/information-technology/2014/07/google-dumps-plans-for-openssl-in-chrome-takes-own-boring-road/)
- <span id="page-14-48"></span>[37] M. Georgiev, S. Iyengar, S. Jana, R. Anubhai, D. Boneh, and V. Shmatikov. The most dangerous code in the world: Validating SSL certificates in non-browser software. In *2012 ACM Conference on Computer and Communications Security*, 2012.
- <span id="page-14-51"></span>[38] D. Gillmor. Negotiated Finite Field Diffie-Hellman Ephemeral Parameters for Transport Layer Security (TLS). IETF RFC 7919, Aug. 2016.
- <span id="page-14-46"></span>[39] GMP-ECM Development Team. GMP-ECM, an implementation of the elliptic curve method for integer factorization, 2016. [http://ecm.gforge.](http://ecm.gforge.inria.fr/) [inria.fr/.](http://ecm.gforge.inria.fr/)
- <span id="page-14-10"></span>[40] D. M. Gordon. Discrete logarithms in GF(p) using the number field sieve. *SIAM Journal of Discrete Math*, 1993.
- <span id="page-14-28"></span>[41] P. Gutmann. Cryptlib, kg\_dlp.c, 2010. [http://www.cypherpunks.to/~peter/](http://www.cypherpunks.to/~peter/cl343_beta.zip) [cl343\\_beta.zip.](http://www.cypherpunks.to/~peter/cl343_beta.zip)
- <span id="page-14-31"></span>[42] O. H., P. S. Dev., H. P., and V. Consortium. Determining strengths for public keys used for exchanging symmetric keys. IETF RFC 3766, Apr. 2004.
- <span id="page-14-14"></span>[43] D. Harkins and D. Carrel. The Internet Key Exchange (IKE). Nov. 1998.
- <span id="page-14-24"></span>[44] C. Hlauschek, M. Gruber, F. Fankhauser, and C. Schanes. Prying open Pandora's box: KCI attacks against TLS. In *9th USENIX Workshop on Offensive Technologies (WOOT '15)*, Aug. 2015.

- <span id="page-14-21"></span>[45] T. Jager, J. Schwenk, and J. Somorovsky. Practical invalid curve attacks on TLS-ECDH. In *20th European Symposium on Research in Computer Security*, 2015.
- <span id="page-14-29"></span>[46] W. Jeffrey. Crypto++, Nov. 2015. [https://github.com/weidai11/](https://github.com/weidai11/cryptopp/blob/48809d4e85c125814425c621d8d0d89f95405924/nbtheory.cpp#L1029) [cryptopp/blob/48809d4e85c125814425c621d8d0d89f95405924/](https://github.com/weidai11/cryptopp/blob/48809d4e85c125814425c621d8d0d89f95405924/nbtheory.cpp#L1029) [nbtheory.cpp#L1029.](https://github.com/weidai11/cryptopp/blob/48809d4e85c125814425c621d8d0d89f95405924/nbtheory.cpp#L1029)
- <span id="page-14-42"></span>[47] Juniper TechLibrary. VPN feature guide for security devices, 2016. [http://www.juniper.net/documentation/en\\_US/junos15.1x49/topics/](http://www.juniper.net/documentation/en_US/junos15.1x49/topics/reference/configuration-statement/security-edit-dh-group.html) [reference/configuration-statement/security-edit-dh-group.html.](http://www.juniper.net/documentation/en_US/junos15.1x49/topics/reference/configuration-statement/security-edit-dh-group.html)
- <span id="page-14-39"></span>[48] C. Kaufman et al. Internet Key Exchange (IKEv2) protocol. IETF RFC 4306, Dec. 2005.
- <span id="page-14-36"></span>[49] C. Kaufman, P. Hoffman, Y. Nir, P. Eronen, and T. Kivinen. Internet Key Exchange protocol version 2 (IKEv2). IETF RFC 7296, Oct. 2014.
- <span id="page-14-0"></span>[50] C. F. Kerry. Digital Signature Standard (DSS). FIPS PUB 186-4, July 2013.
- <span id="page-14-13"></span>[51] T. Kivinen and M. Kojo. More modular exponential (MODP) Diffie-Hellman groups for Internet Key Exchange (IKE). IETF RFC 3526, May 2003.
- <span id="page-14-25"></span>[52] A. Langley, N. Modaduga, and B. Moeller. Transport Layer Security (TLS) False Start. IETF RFC Draft, June 2014.
- <span id="page-14-3"></span>[53] M. Lepinski and S. Kent. Additional Diffie-Hellman groups for use with ietf standards. IETF RFC 5114, 2008.
- <span id="page-14-1"></span>[54] C. H. Lim and P. J. Lee. A key recovery attack on discrete log-based schemes using a prime order subgroup. In *17th International Cryptology Conference*, 1997.
- <span id="page-14-37"></span>[55] D. Maughan, M. Schertler, M. Schneider, and J. Turner. Internet security association and key management protocol ISAKMP. Nov. 1998.
- <span id="page-14-43"></span>[56] Microsoft Windows Networking Team. VPN interoperability guide for Windows Server 2012 R2, 2014. [https://blogs.technet.microsoft.com/](https://blogs.technet.microsoft.com/networking/2014/12/26/vpn-interoperability-guide-for-windows-server-2012-r2/) [networking/2014/12/26/vpn-interoperability-guide-for-windows-server-](https://blogs.technet.microsoft.com/networking/2014/12/26/vpn-interoperability-guide-for-windows-server-2012-r2/)[2012-r2/.](https://blogs.technet.microsoft.com/networking/2014/12/26/vpn-interoperability-guide-for-windows-server-2012-r2/)
- <span id="page-14-47"></span>[57] Nguyen and Shparlinski. The insecurity of the digital signature algorithm with partially known nonces. *Journal of Cryptology*, 15(3):151–176, 2002.
- <span id="page-14-30"></span>[58] A. M. Odlyzko. The future of integer factorization, July 1995. [http://](http://www.dtc.umn.edu/~odlyzko/doc/future.of.factoring.pdf) [www.dtc.umn.edu/~odlyzko/doc/future.of.factoring.pdf.](http://www.dtc.umn.edu/~odlyzko/doc/future.of.factoring.pdf)
- <span id="page-14-12"></span>[59] H. Orman. The Oakley key determination protocol. IETF RFC 2412, Nov. 1998.
- <span id="page-14-38"></span>[60] D. Piper. The Internet IP security domain of interpretation for ISAKMP. IETF RFC 2407, Nov. 1998.
- <span id="page-14-8"></span>[61] S. C. Pohlig and M. E. Hellman. An improved algorithm for computing logarithms over GF(p) and its cryptographic significance. *IEEE Transactions on Information Theory*, 24(1), 1978.
- <span id="page-14-23"></span>[62] W. Polk, R. Housley, and L. Bassham. Algorithms and identifiers for the internet X.509 public key infrastructure certificate and certificate revocation list (CRL) profile. IETF RFC 3279, Apr. 2002.
- <span id="page-14-6"></span>[63] J. M. Pollard. A Monte Carlo method for factorization. *BIT Numerical Mathematics*, 15(3):331–334, 1975.
- <span id="page-14-9"></span>[64] M. J. Pollard. Kangaroos, Monopoly and discrete logarithms. *Journal of Cryptology*, 2000.
- <span id="page-14-50"></span>[65] E. Rescorla. The Transport Layer Security (TLS) protocol version 1.3 draft 16. IETF RFC Draft, Sept. 2016.
- <span id="page-14-4"></span>[66] A. Sanso. OpenSSL Key Recovery Attack on DH small subgroups, Jan. 2016. http://blog.intothesymmetry.com/2016/01/openssl-key-recoveryattack-on-dh-small.html.
- <span id="page-14-7"></span>[67] D. Shanks. Class number, a theory of factorization, and genera. In *Symposia in Pure Math*, volume 20. 1969.
- <span id="page-14-16"></span>[68] Y. Sheffer and S. Fluhrer. Additional Diffie-Hellman tests for the Internet Key Exchange protocol version 2 (IKEv2). IETF RFC 6989, 2013.
- <span id="page-14-17"></span>[69] P. C. Van Oorschot and M. J. Wiener. On Diffie-Hellman key agreement with short exponents. In *EUROCRYPT*, 1996.
- <span id="page-14-44"></span>[70] P. Wouters. 66% of VPN's are not in fact broken, Oct. 2015. [https://nohats.ca/wordpress/blog/2015/10/17/66-of-vpns-are-not](https://nohats.ca/wordpress/blog/2015/10/17/66-of-vpns-are-not-in-fact-broken/)[in-fact-broken/.](https://nohats.ca/wordpress/blog/2015/10/17/66-of-vpns-are-not-in-fact-broken/)
- <span id="page-14-15"></span>[71] T. Ylonen and C. Lonvick. The Secure Shell (SSH) transport layer protocol. IETF RFC 4253, 2006.
```

## File: references/The Elliptic Curve Diffie-Hellman (ECDH).md
```markdown
# The Elliptic Curve Diffie-Hellman (ECDH)

## Rakel Haakegaard and Joanna Lang

### December 2015

### 1 Introduction

Abstract: The Elliptic Curve Diffie-Hellman (ECDH), a variant of the Diffie Hellman, allows two parties that have no prior knowledge of each other to establish a shared secret key over an insecure channel.[3] The Diffie-Hellman works over any group as long as the DLP in the given group is a difficult problem.[2] It is one of the first public key protocols, and it is used to secure a variety of Internet services. However, newly research from October 2015 suggests that the security of Diffie-Hellman key exchange is less secure than widely believed, and maybe not strong enough to prevent very well-funded attacks. We will first discuss the usage and the security of the ECDH specificly, and then look into the newly published article from October 2015 [1] to see if the discoveries that have been made also apply to the ECDH

## 2 Description of ECDH

The Elliptic Curve Diffie Hellman (ECDH) distincts from the general Diffie Hellman (DH) in the way that it is based on the elliptic curve discrete logarithm problem (ECDLP) instead of the discrete logarithm problem (DLP). ECDH is an anonymous key agreement protocol which allows two parties, A and B, to establish a shared secret key over an insecure channel, where each of the parties have an elliptic curve public-private key pair[7] .

The ECDH works as follows. A and B agree on the elliptic curve group E of order n and a primitive element P in E, which then also has the order n. E, n and P are assumed to be known to the adversary. The ECDLP, which the ECDH is based on, is defined as the computation of the integer k given P and Q such that Q = [k]P. The ECDH let A and B compute a shared secret key S, using the property of the ECDLP as described below.

A selects an integer a in the range [2, n − 1], computes Q = [a]P and sends Q to B. B on the other hand selects an integer b in the range [2, n − 1], computes R = [b]P and sends R to A. A and B receives R and Q respectively, and computes the shared secret key S; S = [a]R = [b]Q = [a][b]P = [a ∗ bmod(n)]P. Both A and B get the same value for S, and the shared key is established.[2]

![](_page_0_Figure_10.jpeg)

Figure 1: Elliptic Curve Diffie-Hellman key exchange method[2]

### 3 Security for ECDH

The computational elliptic curve Diffie-Hellman problem (ECDHP) is the problem of trying to find S=[ab mod(n)]P, given E, n, P and the two points Q=[a]P and R=[b]P. This is the problem the adversary will try to solve to get the secret key S, and the ability to defeat this type of attacks is an important part of the security of ECDH.

If the ECDLP in < P > can be efficiently solved, then the ECDHP in < P > can also be efficiently solved by finding a from (P, Q) and then computing S = [a]R. In other words, the ECDHP is no harder than the ECDLP. It is unknown whether the hardness of ECDHP is equal to the hardness of ECDLP. Anyhow, for the ECDHP to have a high degree of security, it is essential that the corresponding ECDLP has a high degree of security. This topic will be discussed in the following section.[8]

### 3.1 Security and hardness of the ECDLP

The elliptic curve parameters for cryptographic schemes should be carefully chosen to be able to resist all known attacks on the ECDLP. The most naive approach for solving the ECDLP is exhaustive search, which can be defeated by choosing a sufficiently large n (n >= 280). The best known attack to the ECDLP is a combination of the Pohlig-Hellman algorithm and Pollard's rho algorithm, with a running time of O( p (p)), with p being the largest prime divisor of n. To defeat this type of attack, one should choose the elliptic curve parameters such that n is divisible by a significantly large prime number p. The size of p should be so large that p (p) steps is an infeasible amount of computation (p >= 2160).[8] The ECDLP is believed to be infeasible by the state of today's computer technology, given that the elliptic curve parameters are carefully chosen to defeat the known attacks to the ECDLP. As of today there has been no discovery of a generalpurpose subexponential-time algorithm for solving the ECDLP.[2]

On the other hand, it should be noted that there is no mathematical proof of that an efficient algorithm for solving the ECDLP does not exist. If someone were to prove that such an efficient polynomial-time algorithm does not exist, this would imply that P 6= NP. This question is as of today known for being one of the most fundamental and outstanding open questions in computer science, so such a proof would be revolutionary (and not very likely to appear). There is either no proof for that the ECDLP is intractable, as ECDLP is not known to be NP-hard. This is not likely to be proved either.[8]

The ECDLP was introduced to computer science only 30 years ago (1985), and because of this it is not as researched as the commonly used DLP, which has a subexponential solution. This, together with the lack of proof for its hardness, are reasons for that some scepticism exist around the security of ECDLP.

### 3.2 Other attacks to ECDH: Man in the middle attack

The ECDH is also concerned with other types of attacks than finding the shared secret key S. One of these is the man-in-the-middle attack, which we will look further into in this section.

A man-in-the-middle attack is an attack where the attacker secretly relays and possibly alters the communication between two parties, while they believe they are directly communication with each other. A third party, who is attacking, retrieves A's public key and sends it's own public key to B. Then, when B transmits his public key, the third party interrupt and substitutes the value with her own public key and sends it to A. Therefore, A has now come to an agreement on a common secret key with the third party instead of B. The exchange can be done in reverse. Therefore it is now possible for the third party to decrypt any messages sent out by A or B. It can read and possibly modify them before the re-encryption with the appropriate key, and then transmit them to the other party.

To address this attacking problem, generally a process of authentication will be needed. The public keys created in the key exchange are either static or ephemeral. A static key is intended for use for a relatively long period of time. Typically, it is intended for use in many instances of a cryptographic key establishment scheme. An ephemeral key is a key which is generated for each execution of a key establishment process. The ephemeral keys are not necessarily authenticated, and this is necessary to avoid man-in-the-middle attack. So, authenticity assurances must be obtained by other means.

If one of A or B's public key is static, man-inthe-middle attacks are thwarted. A secure communication protocol is said to have forward secrecy if compromise of long-term keys does not compromise past session keys. This protects past sessions against future compromises of secret keys or passwords. Static public keys provide neither forward secrecy nor key-compromise impersonation resilience. Therefor, to avoid leaking information about the static private key, holders should validate the other public key and should apply a secure key derivation function to the raw Diffie-Hellman shared secret.[5]

## 4 Usage of ECDH in secure internet protocols

Among other security protocols, the Diffie-Hellman protocol has often been applied to SSL (Security Sockets Layer) and SSH (Secure Shell).

SSL (Security Sockets Layer) is the predecessor to TLS (Transport Layer Security) and they are both referred to as 'SSL'. SSL is the standard security technology developed to establish an encrypted link between a web server and a browser. The link should ensure privacy and integrity of all data passed between the web server and the browser. Before a client and server can begin to exchange information protected by SSL they must exchange or agree upon an encryption key and a cipher to use when encrypting data. The key and chiper must both have high security. Elliptic Curve Diffie-Hellman is one of the secure methods used for the key exchange.

SSL is composed of two layers, the lower layer which manages the symmetric cryptography so the communication is private and reliable, and the upper layer called the handshake protocol. Diffie-Hellman is used in this upper layer. It is possible to use several different Diffie-Hellman methods, in many cases Elliptic Curve Diffie-Hellman is preferable. The handshake allows the server to authenticate itself to the client using publickey techniques. This is also called asymmetric encryption. The key exchange process uses Diffie-Hellman to ensure each party that the other is who they say they are. After this exchange, the keys are computed and the parties begin encrypting all traffic between them, using the computed keys. SSL is among other uses useful for business traffic and to ensure confidentiality, authenticity and integrity.[4]

SHH is a cryptographic network protocol to allow remote login and other network services to operate securely over an unsecured network. It is often used and very common for secure login on the internet. This protocol can automatically encrypt, authenticate and compress transmitted data. SSH proceeds in three stages, the "hello" phase where the first identification is done. In the second stage the parties agree upon a shared secret key. This is where the ECDH method is implemented and used, and the secure key exchanges is done. Ordinary Diffie-Hellman can also be used. At the third and final stage, the shared secret key are used to generate the application keys.

SSH can be used to secure any network service, but common applications are remote command-line login and remote command execution. Among others, SSH can also be used for setting up automatic login to a remote server, for executing a single command on a remote host and secure file transfer.[4][6]

## 5 Article: How Diffie Hellman Fails in Practice

A newly published article from October 2015, written by Adrian, Bhargavan Durumeric et al., states that the Diffie-Hellman key exchange frequently offers less security than widely believed.[1] As previously described, Diffie-Hellman is the main key exchange mechanism in SSH and IPsec and a popular option in SSL, so security flaws related to this method are critical. The author of the article states his conclusion based on an examination of how Diffie-Hellman is commonly implemented and deployed with these protocols.

Mainly there are two reasons for that the Diffie-Hellman offers less security than widely believed. The first reason is that a lot of servers use weak Diffie-Hellman parameters. The second, more critical reason is that many use standardized, hard coded or widely shared Diffie-Hellman parameters. This dramatically reduces the cost of large-scale attacks such that some are within range of feasibility.[1]

The article contains complex discussions about the different attacks to be performed on the internet protocols that use Diffie-Hellman. The problems that are found stem from the fact that the Diffie Hellman (based on discrete log) allows an attacker to perform a single precomputation that only depends on the group. This is a well known fact for cryptographers, but has obviously not been fully understood by system builders.[1] The authors suggests some measures to be taken to defeat the problems in its Recommendations section. This conclusion is of great interest of elliptic curve cryptography, and is stated below.

"Transitioning to elliptic curve Diffie-Hellman (ECDH) key exchange with appropriate parameters avoids all known feasible cryptanalytic attacks."..."We recommend transitioning to elliptic curves where possible; this is the most effective long-term solution to the vulnerabilities described in this paper."[1]

The reason for this recommendation is the fact that current elliptic curve discrete log algorithms for strong curves do not gain as much of an advantage from precomputation. ECDH keys are also shorter than the Diffie Hellman based on "mod p", and the computation of the shared secret key is faster.[1]

### 6 Conclusion

In this report we have discussed the basic properties, the security aspects and the usage of the key agreement protocol Elliptic Curve Diffie Hellman (ECDH).

We divided the security of ECDH into two sections; one concerning the Elliptic Curve Diffie-Hellman problem (ECDHP), and other types of attacks. The ECDHP is essential to the security of the protocol in the way that the adversary shouldn't be able to compute the shared secret key S. The hardness of ECDH is closely related to the corresponding ECDLP, but the equality of the two is not determined. The ECDLP is believed to be infeasible by the state of today's computer technology, but there are some uncertainty associated with it because of the lack of mathematical proof for its hardness.

As a significant example of other types of attacks to the ECDH, we discussed the scenario of a man-in-the-middle attack. An avoiding strategy to this type of attack would in general be a process of authentication.

We also discussed the usage of ECDH in secure Internet protocols. Among other security protocols, the Diffie-Hellman protocols has often been applied to SSL (Security Sockets Layer) and SSH (Secure Shell). The ECDH is believed to be one of the most secure versions of the Diffie-Hellman, and is preferable in many cases.

Finally, we discussed the recently published article "How Diffie-Hellman fails in practice" from 2015. The recommended solution the authors suggests to the problems found, is transitioning to ECDH key exchange whenever possible. With appropriate parameters they state that all known feasible cryptanalytic attacks would be avoided. Based on our discussion for the security of the ECDH, this qualifies as a reasonable solution. On the other hand, because of the uncertainty associated with the ECDH and ECDLP, it may be questioned if this recommendation will be put into practice.

### 7 References

- 1. Adrian, Bhargavan, Durumeric et. al. How Diffie-Hellman Fails in Practice (2015) Available from: https : //weakdh.org/imperfect − forward − secrecy − ccs15.pdf(01 − Nov − 2015)
- 2. Ko¸c, C¸ etin Kaya Elliptic Curve Cryptography Fundamentals. Available from http : //cs.ucsb.edu/ koc/ecc/docx/09ecc.pdf(21− Oct − 2015)
- 3. Diffie–Hellman key exchange (2015) Available from: https : //en.wikipedia.org/wiki/Diff ie
- 4. Ahmed, Sanjabi, Aldiaz et. al. Diffie-Hellman and Its Application in Security Protocols Available from http : //www.ijesit.com/V olume
- 5. Ahmed, Sanjabi, Aldiaz et. al. Man-inthe-middle attack Available from https : //en.wikipedia.org/wiki/M an − in − the − middleattack
- 6. Secure Secure Shell Available from https : //stribika.github.io/2015/01/04/secure − secure − shell.html
- 7. Elliptic Curve Diffie-Hellman Available from https : //en.wikipedia.org/wiki/EllipticcurveDiff ie
- 8. Hankerson et. al. (2004) Guide Elliptic Curve Cryptography University of Waterloo, Springer-Verlag, New York
```

## File: references/The Performance of Elliptic Curve Based Group Diffie-Hellman Protocols for Secure Group Communication over Ad Hoc Networks.md
```markdown
## University of Nebraska - Lincoln

## [DigitalCommons@University of Nebraska - Lincoln](https://digitalcommons.unl.edu/)

CSE Conference and Workshop Papers

[CSE Conference and Workshop Papers](https://digitalcommons.unl.edu/cseconfwork) [Computer Science and Engineering, Department](https://digitalcommons.unl.edu/computerscienceandengineering)  [of](https://digitalcommons.unl.edu/computerscienceandengineering) 

2006

## The Performance of Elliptic Cur formance of Curve Based Gr e Based Group Diffie-Hellman oup Diffie-Hellman Protocols for Secur ocols for Secure Group Communication o oup Communication over Ad Hoc er Ad Hoc Networks

Yong Wang University of Nebraska-Lincoln, ywang@cse.unl.edu

Byrav Ramamurthy University of Nebraska-Lincoln, bramamurthy2@unl.edu

Xukai Zou Indiana University-Purdue University Indianapolis, xkzou@cs.iupui.edu

Follow this and additional works at: [https://digitalcommons.unl.edu/cseconfwork](https://digitalcommons.unl.edu/cseconfwork?utm_source=digitalcommons.unl.edu%2Fcseconfwork%2F105&utm_medium=PDF&utm_campaign=PDFCoverPages) 

![](_page_0_Picture_10.jpeg)

Part of the [Computer Sciences Commons](http://network.bepress.com/hgg/discipline/142?utm_source=digitalcommons.unl.edu%2Fcseconfwork%2F105&utm_medium=PDF&utm_campaign=PDFCoverPages)

Wang, Yong; Ramamurthy, Byrav; and Zou, Xukai, "The Performance of Elliptic Curve Based Group Diffie-Hellman Protocols for Secure Group Communication over Ad Hoc Networks" (2006). CSE Conference and Workshop Papers. 105.

[https://digitalcommons.unl.edu/cseconfwork/105](https://digitalcommons.unl.edu/cseconfwork/105?utm_source=digitalcommons.unl.edu%2Fcseconfwork%2F105&utm_medium=PDF&utm_campaign=PDFCoverPages) 

This Article is brought to you for free and open access by the Computer Science and Engineering, Department of at DigitalCommons@University of Nebraska - Lincoln. It has been accepted for inclusion in CSE Conference and Workshop Papers by an authorized administrator of DigitalCommons@University of Nebraska - Lincoln.

# The Performance of Elliptic Curve Based Group Diffie-Hellman Protocols for Secure Group Communication over Ad Hoc Networks

Yong Wang, Byrav Ramamurthy Department of Computer Science and Engineering University of Nebraska-Lincoln Lincoln, NE 68588 USA Email: {ywang, byrav}@cse.unl.edu

*Abstract***— The security of the two party Diffie-Hellman key exchange protocol is currently based on the discrete logarithm problem (DLP). However, it can also be built upon the elliptic curve discrete logarithm problem (ECDLP). Most proposed secure group communication schemes employ the DLP-based Diffie-Hellman protocol. This paper proposes the ECDLP-based Diffie-Hellman protocols for secure group communication and evaluates their performance on wireless ad hoc networks. The proposed schemes are compared at the same security level with DLP-based group protocols under different channel conditions. Our experiments and analysis show that the Tree-based Group Elliptic Curve Diffie-Hellman (TGECDH) protocol is the best in overall performance for secure group communication among the four schemes discussed in the paper. Low communication overhead, relatively low computation load and short packets are the main reasons for the good performance of the TGECDH protocol.**

## I. INTRODUCTION

Secure group communication (SGC) refers to a scenario in which a group of participants can send and receive messages to/from group members in a way that outsiders are unable to glean any information even when they are able to intercept the messages. The vast majority of SGC protocols use the DLPbased Diffie-Hellman as the basic key agreement protocol [1].

The DLP-based Diffie-Hellman key agreement protocol depends on the discrete logarithm problem for its security. The key length for secure DLP-based Diffie-Hellman has increased over recent years, which has also placed a heavier processing load on applications using DLP-based Diffie-Hellman. However, the processing load is especially critical for ad hoc networks, which have a relatively limited bandwidth, slower CPU speed, limited battery power and high bit-error rate wireless links.

Elliptic Curve Cryptography (ECC) is a public key cryptosystem based on elliptic curves [2], [3]. The attraction of ECC is that it appears to offer equal security for a far smaller key size, thereby reducing processing overhead. However, the methods for computing general elliptic curve discrete logarithms are much less efficient than those for factoring or computing conventional discrete logarithms and it indicates that more computation time is required for ECC. Thus, the overall performance of ECDLP-based applications needs to be evaluated.

Xukai Zou

Department of Computer and Information Science Indiana University-Purdue University Indianapolis Indianapolis, IN 46202 USA Email: xkzou@cs.iupui.edu

The recent work on performance evaluation of group Diffie-Hellman protocols can be found in [4] and [5]. In [4], the authors evaluated five notable group key agreement protocols: Centralized Group Key Distribution (CKD), Burmester Desmedt (BD), Steer et al. (STR), Group Diffie-Hellman (GDH) and Tree based Group Diffie-Hellman (TGDH) concluding that TGDH exhibits the best average performance in high-delay Wide Area Network (WAN). The study in [5] evaluated three Diffie-Hellman based shared key agreement protocols: Group Diffie-Hellman (GDH), Tree-based and Hypercubic Diffie-Hellman demonstrating that GDH is good in ad hoc networks containing less than 100 nodes and TGDH is attractive for larger networks. These papers provide an elegant evaluation of the performance of group Diffie-Hellman protocols. However, few studies have been conducted in literature on the performance of ECDLP-based group Diffie-Hellman protocols.

In this paper, we propose and evaluate the performance of ECDLP-based group Diffie-Hellman protocols for secure group communication under different channel conditions. The rest of the paper is organized as follows. Section 2 describes the background material necessary to understand the ECDLPbased protocols. Section 3 presents the proposed ECDLPbased group schemes. Section 4 analyzes the communication overhead of each protocol and Section 5 describes the experiments and results. Finally, Section 6 concludes the paper.

## II. BACKGROUND

The two party Diffie-Hellman algorithm was presented by Whitfield Diffie and Martin E. Hellman in 1976 [6]. The Diffie-Hellman algorithm depends on the difficulty of computing discrete logarithms. It assumes that all participants know a prime number *p* and a primitive root *g* of *p* (*g<p*).

The Group Diffie-Hellman (GDH) key distribution protocols were first presented in [7]. There are three different versions and we consider GDH.2 in this paper which involves fewer number of rounds and messages than GDH.1 and GDH.3. The GDH protocol consists of two stages: upflow and downflow. The upflow stage collects contributions from all group members. The downflow stage broadcasts the intermediate values to all group members for calculating the shared group key. The

authors in [8] introduced a tree based group Diffie-Hellman protocol which uses a binary tree to minimize the total number of two party exchanges when computing a group key.

## A. Elliptic Curve Cryptography

An Elliptic Curve is usually defined over two finite fields: the prime finite field  $F_p$  containing p elements and the characteristic 2 finite field containing  $2^m$  elements. This paper focuses on the prime finite field.

Let  $F_p$  be a prime finite field so that p is an odd prime number, and let  $a,b \in F_p$  satisfy  $4a^3 + 27b^2 \neq 0 (mod\ p)$ , then an elliptic curve  $E(F_p)$  over  $F_p$  defined by the parameters  $a,b \in F_p$  consists of the set of solutions or points P=(x,y) for  $x,y \in F_p$  to the equation:

$$y^2 = x^3 + ax + b \pmod{p} \tag{1}$$

The equation  $y^2 = x^3 + ax + b \pmod{p}$  is called the defining equation of  $E(F_p)$ . For a given point  $P = (x_P, y_P)$ ,  $x_P$  is called the x-coordinate of P, and  $y_P$  is called the y-coordinate of P.

Cryptographic schemes based on ECC rely on scalar multiplication of elliptic curve points. Given an integer k and a point  $P \in E(F_p)$ , scalar multiplication is the process of adding P to itself k times. The result of this scalar multiplication is denoted  $k \times P$  or kP. Scalar multiplication of elliptic curve points can be computed efficiently using the addition rule together with the double-and-add algorithm or one of its variants.

Consider the equation Q = kP, where  $Q, P \in E_p(a, b)$  and k < p. It is relatively easy to calculate Q given k and P, but it is relatively hard to determine k given Q and P. This is called the discrete logarithm problem for elliptic curves.

Elliptic Curve domain parameters over  $F_p$  are a sextuple,

$$T = (p, a, b, G, n, h)$$

consisting of an integer p specifying the finite field  $F_p$ , two elements  $a, b \in F_p$  specifying an elliptic curve  $E(F_p)$  defined by equation 1, a base point  $G = (x_G, y_G)$  on  $E(F_p)$ , a prime n which is the order of G, and an integer h which is the cofactor  $h = \#E(F_p)/n$ .

SEC2 [9] lists some defined elliptic curve domain parameters over  $F_p$ , which include 112-bit, 128-bit, 160-bit, 192-bit, 224-bit, 256-bit, 384-bit and 521-bit elliptic curve domain parameters. Our simulation is based on these parameters.

## B. Two Party Elliptic Curve Diffie-Hellman Protocol

Similar to DLP-based Diffie-Hellman key exchange agreement, a key exchange between users *A* and *B* using Elliptic Curve Diffie-Hellman (ECDH) can be accomplished as follows:

- 1. A selects an integer  $n_A$  less than p, this is A's private key. A then generates a public key  $P_A = n_A \times G$ ; the public key is a point in  $E_p(a, b)$ .
- 2. B similarly selects a private key  $n_B$  and computes a public key  $P_B = n_B \times G$ .
- 3. A generates the secret key  $K = n_A \times P_B$ . B generates the secret key  $K = n_B \times P_A$ .

The two calculations in step 3 produce the same result because  $n_A \times P_B = n_A \times (n_B \times G) = n_B \times (n_A \times G) = n_B \times P_A$ .

The secret key *K* is a point in the elliptic curve. If this secret key is to be used as a session key, a single integer must be derived. There are two categories of derivation: reversible and irreversible. If the session key is also required to be decoded as a point in elliptic curve, it is reversible. Otherwise, it is irreversible. The reversible derivation will result in a session key which doubles the length of the private key. In the irreversible derivation, we can simply use the *x*-coordinate or simple hash function of the *x*-coordinate as the session key and thus the session key may have a different length with the private key.

## III. PROPOSED ECDLP-BASED SCHEMES

In this section, we propose two ECDLP-based schemes for secure group communication.

## A. Group Elliptic Curve Diffie-Hellman Protocol

The Group Elliptic Curve Diffie-Hellman (GECDH) protocol is an extension of GDH based on ECDLP. GECDH can also be divided into two stages: upflow and downflow. The upflow stage collects contributions from all group members. The downflow stage broadcasts the intermediate values to all group members for calculating the shared group key.

To describe this in more detail, let  $(M_1, M_2, ..., M_n)$  be a group of users, the *i*-th round of upflow stage is as follows:

- 1.  $M_i$ , where  $0 < i \le n$ , receives a sequence of (i-1) intermediate key values  $\{\frac{N_1...N_{i-1}}{N_k}G|k\in[1,i-1]\}$  and one cardinal value  $K_{i-1}=N_1...N_{i-1}G$ .
  - 2.  $M_i$  generates its own contribution  $N_i$ .
  - 3.  $M_i$  computes the new cardinal value  $K_i = N_i K_{i-1}$ .
- 4. The old cardinal value becomes one of the intermediate values.
- 5. Multiply each old intermediate value with  $N_i$  thus producing a set of new intermediate values.
- 6. If i < n,  $M_i$  sends  $K_i$  and the new intermediate values to  $M_{i+1}$ .

In the upflow stage, the intermediate key values and the cardinal value are all points in the elliptic curve and thus they have double the length of the private key. The last cardinal value of the highest-indexed group member  $M_n$  is the secret key. In the last downflow round,  $M_n$  broadcasts n-1 intermediate values to the entire group. Each receiving  $M_i$  identifies its intermediate value and multiples it with  $N_i$  thus computing the secret key. The shared group session key can be derived from the secret key. In our simulation, we use the x-coordinate of the secret key as the shared group key.

## B. Tree-based Group Elliptic Curve Diffie-Hellman Protocol

The proposed protocol, Tree-based group Elliptic Curve Diffie-Hellman (TGECDH), is a variant of TGDH based on ECDLP. In TGECDH, a binary tree is used to organize group members. The nodes are denoted as < l, v>, where  $0 \le v \le 2^l - 1$  since each level l hosts at most  $2^l$  nodes. Each

TABLE I
PROTOCOL COMPARISON (\*SEE DETAILS IN SECTION IV)

|               |       | Rounds | Total messages | Combined message size in bits*                                                |
|---------------|-------|--------|----------------|-------------------------------------------------------------------------------|
| GDH / GECDH   | Join  | n      | n              | $           \frac{k_u}{2}n^2 + (\frac{3k_u}{2} + r)n - 3k_u         $         |
| GDH / GECDH   | Leave | n-1    | n-1            | $           \frac{k_u}{2}(n-1)^2 + (\frac{3k_u}{2} + r)(n-1) - 3k_u         $ |
| TGDH / TGECDH | Join  | 2      | 3              | $2((n+1)h-2^{h}+1)k_u+(n^2-1)c+3(n-1)r$                                       |
| TGDH / TGECDH | Leave | 1      | 1              | $hk_u + r$                                                                    |

node < l, v> is associated with the key  $K_{< l, v>}$  and the blinded key  $BK_{< l, v>} = \mathbb{F}(K_{< l, v>})$  where the function  $\mathbb{F}()$  is scalar multiplication of elliptic curve points in prime field. Assuming a leaf node < l, v> hosts the member  $M_i$ , the node < l, v> has  $M_i's$  session random key  $K_{< l, v>}$ . Furthermore, the member  $M_i$  at node < l, v> knows every key in the key-path from < l, v> to < 0, 0>. Every key  $K_{< l, v>}$  is computed recursively as follows:

$$\begin{array}{rcl} K_{< l, v>} & = & K_{< l+1, 2v>} B K_{< l+1, 2v+1>} \bmod p \\ & = & K_{< l+1, 2v+1>} B K_{< l+1, 2v>} \bmod p \\ & = & K_{< l+1, 2v>} K_{< l+1, 2v+1>} G \bmod p \\ & = & \mathbb{F}(K_{< l+1, 2v>} K_{< l+1, 2v+1>}) \end{array}$$

It is not necessary for the blind key  $BK_{< l,v>}$  of each node to be reversible. Thus, we simply use the x-coordinate of  $K_{< l,v>}$  as the blind key. The group session key can be derived from  $K_{< 0,0>}$ . Each time when there is member join/leave, the sponsor node calculates the group session key first and then broadcasts the new blind keys to the entire group and finally the remaining group members can generate the group session key. Next, we analyze the communication time for each protocol.

## IV. COMMUNICATION ANALYSIS

The group key distribution schemes discussed above are summarized and compared in Table I.

According to Table I, we can calculate the total message size in bits for each protocol. Assume we have  $n \ (n \geq 2)$  participants and let  $k_i, \ k_u$  indicate the private key and the blind key length and r be the overhead of each message. We use f(Join, n) to denote the total message length when n participants establish a group key and use f(Leave, 1) to denote the total message length when the remaining n-1 participants rebuild the group key after an existing member leaves.

Then, in GDH or GECDH, the total message length for n participants to generate the shared key can be calculated as follows:

$$f(Join, n) = (\frac{(n+3)n}{2} - 3)k_u + nr$$
$$= \frac{k_u}{2}n^2 + (\frac{3k_u}{2} + r)n - 3k_u$$

When a member leaves the group, the remaining n-1 participants need to rebuild the group key as n-1 parties build the

group key. Thus,

$$f(Leave, 1) = f(Join, n - 1)$$

$$= \frac{k_u}{2}(n - 1)^2 + (\frac{3k_u}{2} + r)(n - 1) - 3k_u$$
(2)

In tree based group Diffie-Hellman protocol, join and leave have different processing loads. When a new participant joins a group of size i, three messages are required:

- The new participant broadcasts its blind key
- The sponsor node broadcasts the key tree and the blind keys of the nodes which are the siblings of the nodes from the joining member to the root.
- The sponsor node broadcasts the new blind keys to rest of participants

Assuming we need c bits to represent a key tree node when a sponsor node broadcasts the key tree, then, the message size for a new participant to join a group of size i is equal to:

$$m(i) = (1+h+h-1)k_u + (2i-1)c + 3r$$
  
=  $2hk_u + (2i-1)c + 3r$ 

where h is the height of the binary tree and thereby  $h = \lceil \log_2 i \rceil$ .

Therefore, the total message length to build a group of n participants from initial state (including 1 group member) to final state when all participants can generate the group key can be calculated as:

$$f(Join, n) = \sum_{i=2}^{n} m(i) = 2s_n k_u + (n^2 - 1)c + 3(n - 1)r$$

where 
$$s_n = (n+1)h - 2^h + 1$$
 and  $h = \lceil \log_2 n \rceil$ .

When a member leaves the group in tree based group protocols, the sponsor needs to generate a new session key, recalculate the agreed keys and blinds key along the key path and broadcast the new blind keys. Thus, the message size for one member leave is equal to

$$f(Leave, 1) = hk_u + r \tag{3}$$

Let B indicate the bandwidth of the ad hoc network, d be the maximum distance between two participants, s be the number of messages to build a group key for n parties and p be the probability of frames in errors. The communication time can be calculated as:

$$t = \frac{f}{B} \frac{1}{1-p} + \frac{sd}{3 \times 10^8}$$

TABLE II Comparable key sizes

| ECDLP-based scheme<br>(size of n in bits) | DLP-based scheme<br>(modular size in bits) |
|-------------------------------------------|--------------------------------------------|
| 112                                       | 512                                        |
| 160                                       | 1024                                       |
| 224                                       | 2048                                       |
| 256                                       | 3072                                       |
| 384                                       | 7680                                       |
| 512                                       | 15360                                      |

Compared with the transmission time, the propagation delay  $\frac{sd}{3\times 10^8}$  is very small. Thus, we can approximately estimate the communication time as:

$$t \approx \frac{f}{B} \frac{1}{1 - p} \tag{4}$$

Table II shows the comparable key sizes of the same security level for an ECDLP-based group scheme and DLP-based scheme [10]. It shows that ECDLP-based schemes can use a much smaller key size than DLP-based group schemes. In this paper, we evaluate ECDLP-based group Diffie-Hellman schemes at the same security level as the DLP-based Diffie-Hellman schemes. We use the pair  $\langle k, m \rangle$  to represent the security level, where k is the private key size of ECDLP-based scheme and m is the modular size of DLP-based scheme.

TABLE III
KEY SIZE PARAMETERS

|        | $\langle 112 \ bits, 512 \ bits \rangle$ | $k_u$ bits | $\langle 160 \ bits, 1024 \ bits \rangle$ |            |
|--------|------------------------------------------|------------|-------------------------------------------|------------|
|        | $k_i$ bits                               | $k_u$ bits | $k_i$ bits                                | $k_u$ bits |
| GDH    | 512                                      | 512        | 1024                                      | 1024       |
| GECDH  | 112                                      | 232        | 160                                       | 328        |
| TGDH   | 512                                      | 512        | 1024                                      | 1024       |
| TGECDH | 112                                      | 112        | 160                                       | 160        |

Equation 4 is plotted in Figures 1 and 2 for each protocol to show the communication time for member join operations at the level of  $\langle 112\ bits, 512\ bits \rangle$  and  $\langle 160\ bits, 1024\ bits \rangle$ . The bandwidth is set to 11Mbps and the message overhead is set to  $r=192\ bits$  which is the length of a TCP header and each key tree node needs  $c=24\ bits$  for storage when broadcasting. The frames error rate is set to p=8.70%. The key size parameters used in the calculations are shown in Table III.

The figures show that ECDLP-based group schemes have lower communication time than DLP-based group schemes for member join operations. For example, the communication time of GDH is 2.2 times that of GECDH and TGDH is 1.7 times that of TGECDH on average at the level of  $\langle 112\ bits, 512\ bits \rangle$ . Moreover, the advantages increases as the security level increases. At the level of  $\langle 160\ bits, 1024\ bits \rangle$ , the communication load of GDH is 3.1 times that of GECDH and TGDH is 2.4 times that of TGECDH on average.

For member leave operations, the tree-based group Diffie-Hellman schemes are far better than group Diffie-Hellman schemes as shown in equations 2 and 3.

![](_page_4_Figure_10.jpeg)

Fig. 1. Communication time: member join, level  $\langle 112\ bits, 512\ bits \rangle$ . The communication time of GDH is 2.2 times that of GECDH and TGDH is 1.7 times that of TGECDH on average for member join operations.

![](_page_4_Figure_12.jpeg)

Fig. 2. Communication time: member join, level  $\langle 160\ bits, 1024\ bits \rangle$ . The communication time of GDH is 3.1 times that of GECDH and TGDH is 2.4 times that of TGECDH on average for member join operations.

## V. EXPERIMENTS AND DISCUSSION

The experiments were conducted on a Linux box running on a 2.4 GHz Celeron(R) CPU, with 256 MB of memory. Crypo++ Library 5.2.1 [11] was used for the implementation. For each experiment, we ran the protocol ten times and calculated the average. The overall group key generation time includes communication time but does not include individual key generation time which is assumed to be completed in the initial stage. Furthermore, we assume that all the remaining group members can calculate the group key in parallel when  $M_n$  broadcasts n-1 intermediate values to the entire group in the downflow stage of GDH/GECDH or when the sponsor node broadcasts the new blind keys to the entire group in TGDH/TGECDH.

In this paper, we use a two state Markov model to characterize wireless channels. Markov models have been found to be an appropriate model to characterize signal to noise variations in slow fading channels [12], [13]. When used in simulations, the model is usually constructed with two states, each state representing either 'good' or 'bad' channel conditions. All frames received during a 'good' state are assumed to be error free and all frames received during a 'bad' state are assumed to be in error. Let the rate of transition from the good to the bad state be p and the rate of transition from the bad to the good state be q, this model is characterized by computing mean

durations for each state (i.e. 1/p and 1/q) and then using the results as the means for exponential distributed state durations. Table IV shows the mean durations of states as well as the obtained frame error rates from experiments. Two scenarios are considered in the experiments: low bit-error rate channels and high bit-error rate channels.

TABLE IV
CHARACTERIZATION OF THE TWO-STATE MODEL

| Bit<br>error<br>rate<br>(BER) | Transmission rate [Mbps]- frame size [bytes] | Mean good<br>state duration<br>[s] | Mean<br>bad state<br>duration [s] | % of frames in error |
|-------------------------------|----------------------------------------------|------------------------------------|-----------------------------------|----------------------|
| Low                           | 11-1000                                      | 0.0173                             | 0.0015                            | 8.70%                |
| High                          | 11-1000                                      | 0.0027                             | 0.0037                            | 58.30%               |

Figures 3 and 4 show the communication time of the four compared schemes under different channel conditions when the group size is 100. The figures show that TGECDH can tolerate the frame errors in wireless channels.

Figures 5 and 6 show the communication time for member join operations in the experiments as well as the data in Figures 1 and 2 at the level of  $\langle 112\ bits, 512\ bits \rangle$  and  $\langle 160\ bits, 1024\ bits \rangle$ . The experiment results for GDH and GECDH protocols match with the communication analysis well but there is a slight difference for TGDH and TGECDH. This is because TGDH and TGECDH employ short packets and cause less packet loss in the simulation.

Figures 7, 8, 9 and 10 show the overall group key generation time for member join and leave at the level of  $\langle 112\ bits, 512\ bits \rangle$  and  $\langle 160\ bits, 1024\ bits \rangle$ . At the level of  $\langle 112\ bits, 512\ bits \rangle$ , when the group size is less than 62, GDH requires the least key generation time for member join operations. When the group size is more than 62, TGECDH requires the least key generation time. At the level of  $\langle 160\ bits, 1024\ bits \rangle$ , GDH requires the least key generation time for member join operations when group size is less than 25 and TGECDH requires the least key generation time when group size is greater than 25. Figures 8 and 10 indicate that the tree based group schemes are far better than GDH or GECDH for member leave operations.

In Figure 9, when the group size is greater than 70, there are slight fluctuations in the curves. This may be related to the implementation details in the Crypo++ library and is under further investigation.

As for the DLP-based group key agreement protocols, the agreed group key (denoted as GK) size is at least 512 bits in order to have acceptable security level. If GK is used as the secret key to encrypt messages, it is an overkill. Thus, we can assume that from GK, a secret key SK (for example, 128 bits) is derived and the SK is used to encrypt messages.

Similarly, for ECDLP-based group key agreement protocols, we can use GK to derive a SK (128 bits) and use SK to encrypt the messages. In this way, the problem of doubling cipher text length is avoided. In addition, if the GK is used on plain text directly, the plain text needs to be translated to points on the

elliptic curve (i.e., encoding), which is also not an easy task. if a SK derived from GK is used, this translation is avoided.

## VI. CONCLUSIONS

In this paper, we propose and evaluate ECDLP-based Diffie-Hellman protocols for secure group communication in wireless ad hoc networks. The theoretical analysis and experiments show that TGECDH is the best protocol in terms of overall performance for secure group communication in ad hoc networks among the four schemes we discuss in this paper. Although for small group sizes, GDH performs better than TGECDH for member join operations, it takes much more time for GDH to process member leaves than TGECDH while TGECDH performs very well for both member join and leave operations. Moreover, as the key size increases for a higher security level, TGECDH gains more advantages than other schemes.

The good performance of TGECDH over wireless ad hoc networks can be summarized as follows:

- It uses smaller keys.
- It uses less computation time than the DLP-based scheme for the same security level.
- Smaller packets are used to handle high bit error rate wireless links.

## ACKNOWLEDGEMENTS

This work is partially supported by NSF Grant No. CCR-0311577.

## REFERENCES

- [1] X. Zou, B. Ramamurthy, and S. S. Magliveras, *Secure Group Communications Over Data Networks*. Springer, 2005.
- [2] V. S. Miller, "Use of elliptic curves in cryptography," in *Lecture notes in computer sciences*; 218 on Advances in cryptology—CRYPTO 85. New York, NY, USA: Springer-Verlag New York, Inc., 1986, pp. 417–426.
- [3] N. Koblitz, "Elliptic curve cryptosystems," *Mathematics of Computation*, vol. 48, pp. 203–209, 1987.
- [4] Y. Amir, Y. Kim, C. Nita-Rotaru, and G. Tsudik, "On the performance of group key-agreement protocols," in *Proc. of the 22nd IEEE International Conference on Distributed Computing Systems*, Viena, Austria, June 2002.
- [5] K. S. Hagzan and H.-P. Bischof, "The performance of group diffiehellman paradigms," in *The 2004 International Conference on Wireless Networks (ICWN'04)*, Las Vegas, Nevada, USA, June 2004.
- [6] W. Diffie and M. E. Hellman, "New directions in cryptography," *IEEE Transactions on Information Theorey*, vol. 22, no. 6, pp. 644–654, November 1976.
- [7] M. Steiner, G. Tsudik, and M. Waidner, "Diffie-Hellman key distribution extended to group communication," in CCS '96: Proceedings of the 3rd ACM conference on Computer and communications security. New York, NY, USA: ACM Press, 1996, pp. 31–37.
- [8] Y. Kim, A. Perrig, and G. Tsudik, "Simple and fault-tolerant key agreement for dynamic collaborative groups," in CCS '00: Proceedings of the 7th ACM conference on Computer and communications security. New York, NY, USA: ACM Press, 2000, pp. 235–244.
- [9] Recommended Elliptic Curve Domain Parameters, SECG Std. SEC2, 2000, available from www.secg.org/collateral/sec2.pdf.
- [10] Elliptic Curve Cryptography, SECG Std. SEC1, 2000, available from www.secg.org/collateral/sec1.pdf.
- [11] W. Dai, "Crypto++ library 5.2.1," available from www.cryptopp.com.
- [12] C. C. Tan and N. C. Beaulieu, "On first-order Markov modeling for the Rayleigh fading channel," *IEEE Transactions on Communications*, vol. 48, no. 12, pp. 2032–2040, December 2000.
- [13] M. Zorzi, R. R. Rao, and L. B. Milstein, "Error statistics in data transmission over fading channels," *IEEE Transactions on Communications*, vol. 46, no. 11, pp. 1468–1476, November 1998.

![](_page_6_Figure_0.jpeg)

Fig. 3. Communication times under different channel conditions, member join, level 112 *bits,* 512 *bits*-: channel conditions have little effect on TGECDH due to the small size of packets employed.

![](_page_6_Figure_2.jpeg)

Fig. 4. Communication times under different channel conditions, member join, level 160 *bits,* 1024 *bits*-: channel conditions have little affection on TGECDH due to the small size of packets employed.

![](_page_6_Figure_4.jpeg)

Fig. 5. Communication time from analysis and experiments: member join, level 112 *bits,* 512 *bits*-, channel conditions: low, 8.7% frames in error. (a stands for analysis and e stands for experiments.)

![](_page_6_Figure_6.jpeg)

Fig. 6. Communication time from analysis and experiments: member join, level 160 *bits,* 1024 *bits*-, channel conditions: low, 8.7% frames in error. (a stands for analysis and e stands for experiments.)

![](_page_6_Figure_8.jpeg)

Fig. 7. Group key generation time: member join, level 112 *bits,* 512 *bits*-. GDH costs the least key generation time when group size is less than 62 but after that TGECDH costs the least key generation time for member join operations.

![](_page_6_Figure_10.jpeg)

Fig. 8. Group key generation time: member leave, level 112 *bits,* 512 *bits*-. Tree-based group Diffie-Hellman schemes are far better than group Diffie-Hellman schemes for member leave operations.

![](_page_6_Figure_12.jpeg)

Fig. 9. Group key generation time: member join, level 160 *bits,* 1024 *bits*-. GDH costs the least key generation time when group size is less than 25 but after that TGECDH costs the least key generation time for member join operations.

![](_page_6_Figure_14.jpeg)

Fig. 10. Group key generation time: member leave, level 160 *bits,* 1024 *bits*-. Tree-based group Diffie-Hellman schemes are far better than group Diffie-Hellman schemes for member leave operations.
```

## File: references/TLS & Perfect Forward Secrecy.md
```markdown
Once the private key of some HTTPS web site is compromised, an attacker is able to build a [man-in-the-middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack "Man-in-the-middle attack on Wikipedia") to intercept and decrypt any communication with the web site. The first step against such an attack is the revocation of the associated certificate through a CRL or a protocol like OCSP. Unfortunately, the attacker could also have recorded past communications protected by this private key and therefore decrypt them.

_Forward secrecy_ allows today information to be kept secret even if the private key is compromised in the future. Achieving this property is usually costly and therefore, most web servers do not enable it on purpose. Google recently [announced support of forward secrecy](https://security.googleblog.com/2011/11/protecting-data-for-long-term-with.html "Protecting data for the long term with forward secrecy") on their HTTPS sites. Adam Langley [wrote a post with more details on what was achieved](https://www.imperialviolet.org/2011/11/22/forwardsecret.html "Forward secrecy for Google HTTPS") to increase efficiency of such a mechanism: with a few fellow people, he wrote an efficient implementation of some elliptic curve cryptography for OpenSSL.

Update (2019-08)

While the content of this article is still technically sound, ensure you understand it was written by the end of 2011 and therefore doesn’t take into account many important aspects, like the fall of RC4 as an appropriate cipher and the ubiquity of forward secrecy in actual deployments.

-   [Without forward secrecy](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#without-forward-secrecy)
-   [Diffie-Hellman with discrete logarithm](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#diffie-hellman-with-discrete-logarithm)
-   [Diffie-Hellman with elliptic curves](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#diffie-hellman-with-elliptic-curves)
    -   [Some theory](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#some-theory)
    -   [In practice](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#in-practice)
    -   [Some benchmarks](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#some-benchmarks)

## Without forward secrecy

To understand the problem when forward secrecy is absent, let’s look at the classic TLS handshake when using a cipher suite like `AES128-SHA`. During this handshake, the server will present its certificate and both the client and the server will agree on a _master secret_.

![TLS full handshake](https://d2pzklc15kok91.cloudfront.net/images/benchs-ssl/ssl-handshake.10d4a774bb0983.svg)

Full TLS handshake

This secret is built from a 48byte _premaster secret_ generated and encrypted by the client with the public key of the server. It is then sent in a _Client Key Exchange_ message to the server during the third step of the TLS handshake. The _master secret_ is derived from this _premaster secret_ and random values sent in clear-text with _Client Hello_ and _Server Hello_ messages.

This scheme is secure as long as only the server is able to decrypt the _premaster secret_ (with its private key) sent by the client. Let’s suppose that an attacker records all exchanges between the server and clients during a year. Two years later, the server is decommissioned and sent for recycling. The attacker is able to recover the hard drive with the private key. They can now decrypt any session they recorded: the encrypted premaster secret sent by a client is decrypted with the private key and the master secret is derived from it. The attacker can now recover passwords and other sensitive information that can still be valuable today.

The main problem lies in the fact that the private key is used for two purposes: **authentication** of the server and **encryption** of a shared secret. Authentication only matters while the communication is established, but encryption is expected to last for years.

## Diffie-Hellman with discrete logarithm

One way to solve the problem is to keep using the private key for authentication but uses an independent mechanism to agree on a shared secret. Hopefully, there exists a well-known protocol for this: the [Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie-Hellman "Diffie-Hellman key exchange on Wikipedia"). It is a method of exchanging keys without any prior knowledge. Here is how it works in TLS:

1.  The server needs to generate once (for example, with `openssl dhparam` command):
    
    -   $p$, a large [prime number](https://en.wikipedia.org/wiki/Prime_number "Prime numbers on Wikipedia"),
    -   $g$, a [primitive root modulo $p$](https://en.wikipedia.org/wiki/Primitive_root_modulo_n "Primitive root modulo n on Wikipedia")—for every integer $a$ [coprime](https://en.wikipedia.org/wiki/Coprime "Coprime numbers on Wikipedia") to $p$, there exists an integer $k$ such that $g^k\equiv a\pmod{p}$.
2.  The server picks a random integer $a$ and compute $g^a \bmod     p$. After sending its regular _Certificate_ message, it will also send a _Server Key Exchange_ message (not included in the handshake depicted above) containing, unencrypted but signed with its private key for authentication purpose:
    
    -   random value from the _Client Hello_ message,
    -   random value from the _Server Hello_ message,
    -   $p$, $g$,
    -   $g^a\bmod p=A$.
3.  The client checks that the signature is correct. It also picks a random integer $b$ and sends $g^b \bmod p=B$ in a _Client Key Exchange_ message. It will also compute $A^b\bmod p=g^{ab}\bmod p$ which is the _premaster secret_ from which the _master secret_ is derived.
    
4.  The server will receive $B$ and compute $B^a\bmod p=g^{ab}\bmod p$ which is the same _premaster secret_ known by the client.
    

Again, the private key is only used for authentication purpose. An eavesdropper will only know $p$, $g$, $g^a\bmod p$ and $g^b\bmod p$. Computing $g^{ab}\bmod p$ from these values is the [discrete logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm "Discrete Logarithm on Wikipedia") problem for which there is no known efficient solution.

Because the Diffie-Hellman exchange described above always uses new random values $a$ and $b$, it is called _Ephemeral Diffie-Hellman_ (EDH or DHE). Cipher suites like `DHE-RSA-AES128-SHA` use this protocol to achieve _perfect forward secrecy_.<sup id="fnref-pfs"><a href="https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#fn-pfs">1</a></sup>

To achieve a good level of security, parameters of the same size as the key are usually used (the security provided by the discrete logarithm problem is about the same as the security provided by factorisation of two large prime numbers) and therefore, the exponentiation operations are pretty slow as we can see in the benchmark below:

![Graphical comparison of speed with and without DHE](https://d2pzklc15kok91.cloudfront.net/images/benchs-ssl/dhe-impact.0f97592a621f2c.png)

Performances of stud on 6 cores, with and without DHE with a 1024-bit key

Update (2015-05)

The [Logjam attack](https://weakdh.org/ "Logjam: How Diffie-Hellman Fails in Practice") demonstrated that the security of Diffie-Hellman is lower than expected, notably when the prime is shared by many servers as this is usually the case. In this case, an attack against this prime can be precomputed and used to efficiently break connections using the same prime. Ensure that the DH parameter matches the size of the associated RSA key (at least 2048 bits).

## Diffie-Hellman with elliptic curves

Fortunately, there exists another way to achieve a Diffie-Hellman key exchange with the help of [elliptic curve cryptography](https://en.wikipedia.org/wiki/Elliptic_curve_cryptography "Elliptic curve cryptography on Wikipedia") which is based on the algebraic structure of elliptic curves over finite fields. To get some background on this, be sure to check first [Wikipedia article on elliptic curves](https://en.wikipedia.org/wiki/Elliptic_curve "Elliptic curves on Wikipedia"). Elliptic curve cryptography allows one to achieve the same level of security than RSA with smaller keys. For example, a 224-bit elliptic curve is believed to be [as secure as a 2048-bit RSA key](https://www.keylength.com/en/compare/ "Cryptographic key length recommendation").

## Some theory

Diffie-Hellman key exchange described above can easily be translated to elliptic curves. Instead of defining $p$ and $g$, you get some elliptic curve, $y^2=x^3+\alpha x+\beta$, a prime $p$ and a base point $G$. All these parameters are public. In fact, while they can be generated by the server, this is a difficult operation and they are usually chosen among a set of published ones.

The use of elliptic curves is an extension of TLS described in [RFC 4492](https://www.rfc-editor.org/rfc/rfc4492 "RFC 4492: ECC Cipher Suites for TLS"). Unlike with the classic Diffie-Hellman key exchange, the client and the server need to agree on the various parameters. Most of this agreement is done inside _Client Hello_ and _Server Hello_ messages. While it is possible to define some arbitrary parameters, web browsers will only support a handful of predefined curves, usually NIST P-256, P-384 and P-521. From here, the key exchange with elliptic curves is pretty similar to the classic Diffie-Hellman one:

1.  The server picks a random integer $a$ and compute $aG$ which will be sent, unencrypted but signed with its private key for authentication purpose, in a _Server Key Exchange_ message.
2.  The client checks that the signature is correct. It also picks a random integer $b$ and sends $bG$ in a _Client Key Exchange_ message. It will also compute $b\cdot aG=abG$ which is the _premaster secret_ from which the _master secret_ is derived.
3.  The server will receive $bG$ and compute $a\cdot bG=abG$ which is the same _premaster secret_ known by the client.

An eavesdropper will only see $aG$ and $bG$ and won’t be able to compute efficiently $abG$.

Using `ECDHE-RSA-AES128-SHA` cipher suite (with P-256 for example) is already a huge speed improvement over `DHE-RSA-AES128-SHA` thanks to the reduced size of the various parameters involved.

Web browsers only support a handful of well-defined elliptic curves, chosen to ease an efficient implementation. Bodo Möller, Emilia Käsper and Adam Langley have provided 64-bit optimized versions of NIST P-224, P-256 and P-521 for OpenSSL. To get even more details on the matter, you can read the end of the [introduction on elliptic curves](https://www.imperialviolet.org/2010/12/04/ecc.html "Elliptic curves and their implementation") from Adam Langley, then a [short paper from Emilia Käsper](http://research.google.com/pubs/archive/37376.pdf "Fast Elliptic Curve Cryptography in OpenSSL") which presents a 64-bit optimized implementation of the NIST elliptic curve NIST P-224.

## In practice

First, keep in mind that elliptic curve cryptography is not supported by all browsers. Recent versions of Firefox and Chrome should handle NIST P-256, P-384 and P-521 but for Internet Explorer on Windows XP, you are currently out of luck. Therefore, you need to keep accepting other cipher suites.

You need a recent version of OpenSSL. Support for ECDHE cipher suites has been added in **OpenSSL 1.0.0**. Check with `openssl ciphers ECDH` that your version supports them. If you want to use the 64-bit optimized version, you need to run a snapshot of OpenSSL 1.0.1, configured with `enable-ec_nistp_64_gcc_128` option. A recent GCC is also required in this case.

Next, you need to choose the appropriate **cipher suites**. If forward secrecy is an option for you, you can opt for `ECDHE-RSA-AES128-SHA:AES128-SHA:RC4-SHA` cipher suites which should be compatible with most browsers. If you really need forward secrecy, you may opt for `ECDHE-RSA-AES128-SHA:DHE-RSA-AES128-SHA:EDH-DSS-DES-CBC3-SHA` instead.

Then, you need to ensure the **order of cipher suites is respected**. On _nginx_, this is done with `ssl_prefer_server_ciphers on`. On _Apache_, this is `SSLHonorCipherOrder on`.

Update (2011-11)

You need to check **ECDHE support for your web server**. For _nginx_, the support has been added in 1.0.6 and 1.1.0. The curve selected defaults to NIST P-256. You can specify another one with `ssl_ecdh_curve` directive. For _Apache_, it has been added in 2.3.3 and does not exist in the current stable branch. Adding support for ECDHE is quite easy. You can check [how I added it in _stud_](https://github.com/bumptech/stud/pull/61 "Adding support for ECDHE in stud"). This issue also exists for DHE cipher suites, in which case you also might have to specify DH parameters to use (generated with `openssl dhparam`) using some special directive or by appending the parameters to the certificate. Check [Immerda Techblog article](https://tech.immerda.ch/2011/11/the-state-of-forward-secrecy-in-openssl/ "The state of Forward Secrecy in OpenSSL") for more background about this point.

The implementation of [TLS session tickets](https://vincent.bernat.ch/en/blog/2011-ssl-session-reuse-rfc5077 "Speeding up TLS: enabling session reuse") may be incompatible with forward secrecy, depending on how they are implemented. When they are protected by a random key generated at the start of the server, the same key could be used for months. Some implementations<sup id="fnref-stud"><a href="https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy#fn-stud">2</a></sup> may derive the key from the private key. In this case, forward secrecy is broken. If forward secrecy is a requirement for you, you need to either disable tickets or ensure that key rotation happens often.

Check with `openssl s_client -tls1 -cipher ECDH -connect 127.0.0.1:443` that everything works as expected.

## Some benchmarks

With the help of the [micro-benchmark tool](https://github.com/vincentbernat/ssl-dos/blob/master/server-vs-client.c "Tool compare processing power needed by client and server") that I developed for my [previous article](https://vincent.bernat.ch/en/blog/2011-ssl-dos-mitigation "TLS computational DoS mitigation"), we can compare the efficiency of cipher suites providing forward secrecy:

![Speed comparison with/without DHE/ECDHE](https://d2pzklc15kok91.cloudfront.net/images/benchs-ssl/ecdhe.49e6b1ed22b02e.png)

Compared performance for 1000 handshakes of various cipher suites (RSA 2048, DHE, ECDHE, optimized ECDHE)

I have used a snapshot of OpenSSL 1.0.1 (2011/11/25). The optimized version of ECDHE is the one you get by using `enable-ec_nistp_64_gcc_128` option when configuring OpenSSL.

Let’s focus on the server part. Enabling `DHE-RSA-AES128-SHA` cipher suite hinders the performance of TLS handshakes by a factor of 3. Using `ECDHE-RSA-AES128-SHA` instead only adds an overhead of 27%. However, if we use the 64-bit optimized version, the **cost is only 15%**. The overhead is only per full TLS handshake. If 3 out of 4 of your handshakes are resumed, you need to adjust the numbers.

Your mileage may vary but the computational cost for enabling perfect forward secrecy with an ECDHE cipher suite seems a small sacrifice for better security.
```

## File: Implementation-Plan-Task-Lists.md
```markdown
## Project Implementation Plan
**`Title`**: Diffie-Hellman Anahtar Değişim Protokolü: Güvensiz Bir Kanalda Güvenli Anahtar Oluşturmanın Görsel Simülasyonu ve MitM Zafiyet Analizi 
**`Strategy`**: Build, Measure, Break & Simulate

---

## 1. Project Objective
To transition from a theoretical simulation to a **technical demonstration** by implementing cryptographic primitives from scratch, rigorously benchmarking their performance in a controlled environment, and demonstrating real-world vulnerabilities (MitM and Forward Secrecy failures) as cited in academic literature.

---

## 2. Architecture OverviewThe software will consist of three distinct modules:

1. **`crypto_engine/`**: The "No Libraries" core implementing raw mathematical algorithms.
2. **`benchmark_suite/`**: The scientific testing harness running inside Docker.
3. **`attack_lab/`**: The demonstration environment for MitM and Forward Secrecy exploits.

---

## Phase 1: Build (The "No Libraries" Math Engine)
*Goal: Address the critique "Build the algorithms yourself" by implementing core logic without `pow()` or OpenSSL.*

### **A. Modular Arithmetic (Classic DH)**
* [x] **Implement `square_and_multiply(base, exponent, modulus)`:**
* **Logic:** Convert exponent to binary. Iterate bits: square the current value, and if the bit is `1`, multiply by the base. Apply modulo at every step.
* **Purpose:** Demonstrates the O(\log n) efficiency required for large primes (e.g., 2048-bit).


###**B. Elliptic Curve Arithmetic (ECDH)**
* [x] **Define `EllipticCurve` Class:**
* Parameters: a, b, p (Equation: y^2 = x^3 + ax + b \pmod p).


* [x] **Implement `point_add(P, Q)`:**
* Geometric addition logic (slope calculation over finite field).


* [x] **Implement `point_double(P)`:**
* Tangent line logic for adding a point to itself.


* [x] **Implement `scalar_multiply(k, P)`:**
* **Logic:** The "Double-and-Add" algorithm (analogous to Square-and-Multiply).

**Purpose:** This is the core performance engine for ECDH.

### **C. Protocol Logic**
* [x] **Static DH:** Hardcoded private keys (a) for demonstrating lack of Forward Secrecy.
* [x] **DHE (Ephemeral):** Generates new random a per session.
* [x] **ECDHE:** Generates new random private scalar k per session using the `EllipticCurve` class.

---

## Phase 2: Measure (The Scientific Benchmark)
*Goal: Address the critique "How did you come to that conclusion?" regarding efficiency using reproducible experiments.*

### **A. Experimental Environment (Docker)**
* [x] **Create `Dockerfile`:**
* Base Image: `python:3.9-slim`
* Purpose: Ensures the teacher can replicate exact results.

* [x] **Resource Constraints (The "Ad Hoc Network" Sim):**
* 
* **Scenario A (IoT Node):** Run with `docker run --cpus="0.5" --memory="128m"` to simulate limited hardware.

* **Scenario B (Standard Server):** Run with `docker run --cpus="2.0" --memory="1g"`.


### **B. The Benchmark Script**
* [x] Define Security Equivalences:
* **Test 1:** DH-2048 vs. ECDH-224 (112-bit security).
* **Test 2:** DH-3072 vs. ECDH-256 (128-bit security).


* [x] **Metrics to Record:**
* **Wall-clock Time:** Time taken to generate Key Pair + Compute Shared Secret.
* **Bandwidth:** Size of Public Key (A vs. Point P) in bytes.


* [x] **Output:** Generate CSV data to produce a bar chart showing DH latency growing exponentially while ECDH remains linear.

---

## Phase 3: Break (Vulnerability Analysis)
*Goal: Address "Ground findings in real-world data" by replicating specific attacks found in literature.*

### **A. Forward Secrecy "Time Travel" Demo**
* [ ] **The Setup:** A `SessionLogger` records encrypted transcripts of 5 distinct chat sessions.
* [ ] **Attack Scenario 1 (Static DH):**
* Action: Leak the long-term private key.
* Result: Decrypt **all 5** past sessions from the log.
* Context: "Static public keys provide neither forward secrecy... nor key-compromise resilience".

* [ ] **Attack Scenario 2 (ECDHE):**
* Action: Leak the private key from Session #5.
* Result: Decrypt Session #5, but **fail** to decrypt Sessions #1-4.
* Context: Proves that compromising keys does not compromise past session keys.


### **B. Small Subgroup Confinement Attack (MitM)**
* [ ] **Vulnerable Implementation:** Create a "burak" node that receives public key A but **skips** validating if A is a valid group generator.
* [ ] **The Attack Vector:**
* **Mallory:** Intercepts arda's key.

**Injection:** Replaces it with p-1 (order 2 subgroup generator).

* [ ] **The Exploit:**
* burak computes S = (p-1)^b \pmod p.
* Result: S is forced to be either `1` or `-1`.
* Mallory brute-forces the message by trying only these 2 keys.


* [ ] **Real-World Context:** Cite that 88% of Amazon Load Balancers were found vulnerable to parameter reuse/validation issues.

---

## 4. Presentation Deliverables Checklist
| Segment | Artifact to Show | Purpose |
| --- | --- | --- |
| **Implementation** | Code walk-through of `scalar_multiply` (Double-and-Add). | Prove you built the math yourself. |
| **Efficiency** | Graph: "Execution Time: DH vs ECDH" (generated from Docker). | Provide concrete experimental data. |
| **Security (FS)** | Console Log: "Session 1 Decryption FAILED" (after key leak). | Visual proof of Forward Secrecy. |
| **Security (MitM)** | Live Demo: Decrypting a message using the key `1`. | Demonstrate the "Small Subgroup" attack. |

---

* [ ] Cite all academic papers that informed your implementation, measurements, and attack simulations.

## 5. References & Citations (All reference research project documents can be found in the `references/` folder)
* **[1] Efficiency:** *The Performance of Elliptic Curve Based Group Diffie-Hellman Protocols* (Wang et al.) - Used for defining testbed constraints and security equivalence levels.
* **[2] MitM Vulnerability:** *Measuring Small Subgroup Attacks Against Diffie-Hellman* (Valenta et al.) - Used for the Subgroup Confinement Attack logic.
* **[3] Forward Secrecy:** *The Elliptic Curve Diffie-Hellman (ECDH)* (Haakegaard & Lang) - Used for defining static vs. ephemeral key definitions.
* **[4] Diffie-Hellman:** *Authenticated Key Exchange Provably Secure against the MiTM Attack* (Ann & Peter)
```

## File: attack_lab/forward_secrecy.py
```python
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol
from benchmark_suite.standard_params import DH_2048_P, DH_2048_G
from attack_lab.utils import *


def run_forward_secrecy_demo():
    log_title("SCENARIO A: Forward Secrecy Analysis")

    # ==========================================
    # PART 1: THE STATIC KEY DISASTER
    # ==========================================
    print(f"{Colors.BOLD}--- Simulation 1: Static DH (No Forward Secrecy) ---{Colors.RESET}")

    # 1. Setup Static Server (burak uses Long Term Key)
    burak_static = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    log_actor("Server(burak)", "Initialized with STATIC Private Key", f"Key: {str(burak_static._private_key)[:10]}...")

    # 2. Simulate Past Traffic (Session 1 - Yesterday)
    arda_v1 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)  # arda is ephemeral

    # Handshake
    s1_secret = burak_static.generate_shared_secret(arda_v1.public_key)
    s1_msg = "My password is 'hunter2'"
    s1_cipher = simple_xor_encrypt(s1_msg, s1_secret)

    log_actor("arda", "Sent Encrypted Msg (Session 1)", f"Ciphertext: {s1_cipher.hex()[:20]}...", Colors.BLUE)

    # 3. Simulate Traffic (Session 2 - Today)
    arda_v2 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)

    # Handshake
    s2_secret = burak_static.generate_shared_secret(arda_v2.public_key)
    s2_msg = "Attack at dawn"
    s2_cipher = simple_xor_encrypt(s2_msg, s2_secret)

    log_actor("arda", "Sent Encrypted Msg (Session 2)", f"Ciphertext: {s2_cipher.hex()[:20]}...", Colors.BLUE)

    # 4. THE LEAK (Mallory hacks the server TODAY)
    leaked_private_key = burak_static._private_key
    log_attack("SERVER COMPROMISED!", f"Leaked Key: {str(leaked_private_key)[:10]}...")

    # 5. The Exploit (Time Travel)
    # Mallory uses the key stolen TODAY to decrypt Session 1 (YESTERDAY)
    print(f"\n{Colors.RED}Mallory attempts to decrypt PAST Session 1 logs...{Colors.RESET}")

    # Mallory reconstructs the secret: (arda_Public_V1 ^ Leaked_burak_Priv) % P
    mallory_s1_calc = pow(arda_v1.public_key, leaked_private_key, DH_2048_P)
    decrypted_s1 = simple_xor_decrypt(s1_cipher, mallory_s1_calc)

    if decrypted_s1 == s1_msg:
        log_attack("DECRYPTION SUCCESSFUL", f"Recovered Past Msg: '{decrypted_s1}'")
        print(f"{Colors.RED}>> CRITICAL FAILURE: Compromise of current key exposed past data.{Colors.RESET}\n")
    else:
        print("Decryption Failed.")

    # ==========================================
    # PART 2: THE EPHEMERAL FIX (DHE)
    # ==========================================
    print(f"{Colors.BOLD}--- Simulation 2: Ephemeral DH (Perfect Forward Secrecy) ---{Colors.RESET}")

    # 1. Session 1 (Yesterday) - burak uses Ephemeral Key A
    burak_eph_1 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    arda_eph_1 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    s1_secret = burak_eph_1.generate_shared_secret(arda_eph_1.public_key)
    s1_cipher = simple_xor_encrypt("Nuclear Launch Codes: 0000", s1_secret)

    log_actor("System", "Session 1 Complete", "Keys destroyed from memory.", Colors.YELLOW)

    # 2. Session 2 (Today) - burak uses Ephemeral Key B
    burak_eph_2 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)  # NEW KEY!
    arda_eph_2 = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    s2_secret = burak_eph_2.generate_shared_secret(arda_eph_2.public_key)

    # 3. THE LEAK (Mallory hacks server TODAY)
    # She only gets the key currently in memory (Session 2's key)
    leaked_key_today = burak_eph_2._private_key
    log_attack("SERVER COMPROMISED!", f"Leaked Key (Session 2): {str(leaked_key_today)[:10]}...")

    # 4. The Exploit Attempt
    print(f"\n{Colors.RED}Mallory attempts to decrypt PAST Session 1 logs...{Colors.RESET}")

    # Mallory tries to use Today's key on Yesterday's traffic
    mallory_fail_calc = pow(arda_eph_1.public_key, leaked_key_today, DH_2048_P)
    decrypted_attempt = simple_xor_decrypt(s1_cipher, mallory_fail_calc)

    if decrypted_attempt != "Nuclear Launch Codes: 0000":
        print(f"{Colors.GREEN}{Colors.BOLD}>> DECRYPTION FAILED!{Colors.RESET}")
        print(f"   Garbage Output: {decrypted_attempt[:20]}...")
        log_actor("System", "Forward Secrecy Verified", "Past secrets remain secure.", Colors.GREEN)


if __name__ == "__main__":
    run_forward_secrecy_demo()
```

## File: attack_lab/subgroup_mitm.py
```python
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol
from crypto_engine.modular_arithmetic import ModularArithmetic
from benchmark_suite.standard_params import DH_2048_P, DH_2048_G
from attack_lab.utils import *


class NaiveBurak(DiffieHellmanProtocol):
    """
    A Vulnerable Implementation of burak.
    He forgot to check if the public key is in range [2, p-2].
    """

    def generate_shared_secret(self, other_public_key: int) -> int:
        # VULNERABILITY: No check for small subgroup attacks!
        # Normal code would raise Error if other_public_key == p-1

        # Just compute straight away
        shared_secret = ModularArithmetic.square_and_multiply(other_public_key, self._private_key, self.p)
        return shared_secret


def run_mitm_demo():
    log_title("SCENARIO B: Small Subgroup Confinement Attack")

    # 1. Setup
    p = DH_2048_P
    g = DH_2048_G

    # Naive burak is initialized
    burak = NaiveBurak(p, g)
    log_actor("burak (Naive)", "Waiting for arda's Public Key...", "", Colors.GREEN)

    # 2. Mallory Intercepts
    log_actor("arda", "Sends Public Key A", "Points to -> burak", Colors.BLUE)
    log_attack("INTERCEPTION", "Mallory blocks arda's key.")

    # 3. Injection (The Attack)
    # Mallory sends p-1 (which is -1 mod p). This has Order 2.
    # The result will be (-1)^b.
    # If b is even -> 1. If b is odd -> p-1.
    malicious_key = p - 1
    log_attack("INJECTION", f"Mallory sends (P - 1) to burak.")

    # 4. burak Computes Shared Secret
    # burak thinks 'malicious_key' is arda.
    try:
        buraks_secret = burak.generate_shared_secret(malicious_key)
        log_actor("burak (Naive)", "Computes Shared Secret", f"Value: {str(buraks_secret)[:10]}... (Hidden)", Colors.GREEN)

        # burak encrypts sensitive data
        secret_msg = "Launch Missiles at 12:00"
        ciphertext = simple_xor_encrypt(secret_msg, buraks_secret)
        log_actor("burak (Naive)", "Sends Encrypted Data", f"Bytes: {ciphertext.hex()[:20]}...", Colors.GREEN)

    except ValueError as e:
        print("burak detected the attack! (This shouldn't happen in NaiveBurak)")
        return

    # 5. Mallory Brute Forces
    print(f"\n{Colors.RED}Mallory starts Brute Force...{Colors.RESET}")
    log_actor("Mallory", "Analyzing Subgroup...", "Generator order is 2. Search space size: 2 keys.", Colors.RED)

    # There are only 2 possible secrets: 1 or p-1
    possible_keys = [1, p - 1]

    for candidate_key in possible_keys:
        print(f"  Trying Candidate Key: {str(candidate_key)[:10]}...", end=" ")

        # Attempt decrypt
        decrypted = simple_xor_decrypt(ciphertext, candidate_key)

        # Check if it looks like English text (simple heuristic)
        if "Missiles" in decrypted:
            print(f"{Colors.GREEN}[MATCH FOUND]{Colors.RESET}")
            log_attack("CRACKED", f"Message: '{decrypted}'")
            print(f"{Colors.RED}>> ATTACK SUCCESS: 2048-bit security reduced to 2 guesses.{Colors.RESET}")
            break
        else:
            print(f"{Colors.YELLOW}[FAIL]{Colors.RESET}")


if __name__ == "__main__":
    run_mitm_demo()
```

## File: attack_lab/utils.py
```python
import sys
import hashlib


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'  # arda
    GREEN = '\033[92m'  # burak
    RED = '\033[91m'  # Mallory/Attacker
    YELLOW = '\033[93m'  # System/Info
    BOLD = '\033[1m'
    RESET = '\033[0m'


def log_title(title):
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== {title} ==={Colors.RESET}")
    print(f"{Colors.HEADER}{'=' * (len(title) + 8)}{Colors.RESET}\n")


def log_actor(name, action, detail="", color=Colors.RESET):
    print(f"{color}{Colors.BOLD}[{name}]{Colors.RESET} {action}")
    if detail:
        print(f"    {Colors.YELLOW}↳ {detail}{Colors.RESET}")


def log_attack(action, result):
    print(f"{Colors.RED}{Colors.BOLD}[ATTACK]{Colors.RESET} {action}")
    print(f"    {Colors.RED}↳ RESULT: {result}{Colors.RESET}")


def simple_xor_encrypt(message: str, shared_secret_int: int) -> bytes:
    """
    A toy encryption for demonstration.
    Hashes the integer shared secret to get a key, then XORs the message.
    """
    # 1. Derive a key from the shared secret integer
    key_hash = hashlib.sha256(str(shared_secret_int).encode()).digest()

    # 2. XOR encrypt
    msg_bytes = message.encode()
    encrypted = bytearray()
    for i, b in enumerate(msg_bytes):
        encrypted.append(b ^ key_hash[i % len(key_hash)])
    return bytes(encrypted)


def simple_xor_decrypt(ciphertext: bytes, shared_secret_int: int) -> str:
    """Decrypts the XOR message."""
    key_hash = hashlib.sha256(str(shared_secret_int).encode()).digest()
    decrypted = bytearray()
    for i, b in enumerate(ciphertext):
        decrypted.append(b ^ key_hash[i % len(key_hash)])
    return decrypted.decode('utf-8', errors='ignore')
```

## File: attack_visualizer/static/script.js
```javascript
const socket = io();

// UI Elements
const packet = document.getElementById('active-packet');
const logContainer = document.getElementById('log-container');
const malloryNode = document.getElementById('node-mallory');

// --- Control Functions ---
function startHandshake(type) {
    socket.emit('init_handshake', {type: type});
}

function toggleAttack() {
    socket.emit('toggle_attack');
}

function leakKey() {
    socket.emit('leak_key');
}

// --- WebSocket Handlers ---

socket.on('log', (data) => {
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    const time = new Date().toLocaleTimeString();
    entry.innerHTML = `<span class="log-time">[${time}]</span> <span class="log-source">${data.source}:</span> ${data.msg}`;
    logContainer.prepend(entry);
});

socket.on('update_mallory', (data) => {
    if(data.active) {
        malloryNode.classList.add('active');
        document.getElementById('status-mallory').innerText = "Mode: INTERCEPTING";
    } else {
        malloryNode.classList.remove('active');
        document.getElementById('status-mallory').innerText = "Mode: Passive";
    }
});

socket.on('anim_packet', (data) => {
    // Show packet
    packet.style.opacity = '1';
    packet.innerHTML = `<i class="fas fa-key"></i>`;
    packet.style.left = '10%'; // Start at arda
    packet.style.transition = 'none';

    // Trigger Reflow
    void packet.offsetWidth;

    // Animate
    packet.style.transition = 'left 2s ease-in-out';

    if (data.intercepted) {
        // Stop at Mallory
        packet.style.left = '50%';
        setTimeout(() => {
            packet.innerHTML = `<i class="fas fa-skull"></i>`; // Change to malicious
            packet.style.backgroundColor = '#da3633';
            packet.style.color = '#fff';

            // Resume to burak after brief pause
            setTimeout(() => {
                packet.style.left = '90%';
                setTimeout(() => {
                    packet.style.opacity = '0';
                    socket.emit('complete_handshake'); // Tell server animation is done
                }, 2000);
            }, 1000);
        }, 2000);
    } else {
        // Go straight to burak
        packet.style.left = '90%';
        setTimeout(() => {
            packet.style.opacity = '0';
            socket.emit('complete_handshake');
        }, 2000);
    }
});

socket.on('update_status', (data) => {
    const el = document.getElementById(`status-${data.actor}`);
    const keyEl = document.getElementById(`key-${data.actor}`);

    el.innerText = data.status.toUpperCase();
    keyEl.innerText = `Secret: ${data.secret}`;

    if (data.status === 'compromised') el.style.color = '#da3633';
    if (data.status === 'secure') el.style.color = '#2ea043';
});

socket.on('anim_leak', (data) => {
    const burak = document.getElementById('node-burak');
    burak.style.boxShadow = "0 0 30px #da3633";
    setTimeout(() => { burak.style.boxShadow = "none"; }, 500);
});
```

## File: attack_visualizer/static/style.css
```css
body {
    background-color: #0d1117;
    color: #c9d1d9;
    font-family: 'Consolas', 'Courier New', monospace;
    margin: 0;
    padding: 20px;
}

.header {
    text-align: center;
    border-bottom: 1px solid #30363d;
    padding-bottom: 20px;
    margin-bottom: 40px;
}

.highlight { color: #58a6ff; }

.controls button {
    background: #21262d;
    border: 1px solid #30363d;
    color: white;
    padding: 10px 20px;
    margin: 0 5px;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s;
}

.controls button:hover { background: #30363d; }
.controls .btn-red { border-color: #da3633; color: #da3633; }
.controls .btn-red:hover { background: #da3633; color: white; }
.controls .btn-warning { border-color: #d29922; color: #d29922; }

/* NETWORK GRID */
.network-grid {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 20px;
    height: 400px;
    align-items: center;
}

.node {
    background: #161b22;
    border: 1px solid #30363d;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    position: relative;
    transition: transform 0.3s;
}

.node.attacker {
    border-color: #da3633;
    opacity: 0.5;
}
.node.attacker.active {
    opacity: 1;
    box-shadow: 0 0 20px rgba(218, 54, 51, 0.4);
}

.icon { font-size: 3em; margin-bottom: 10px; }
#node-arda .icon { color: #58a6ff; }
#node-burak .icon { color: #2ea043; }
#node-mallory .icon { color: #da3633; }

.key-display {
    background: #0d1117;
    padding: 5px;
    font-size: 0.8em;
    color: #8b949e;
    margin-top: 10px;
    border-radius: 4px;
}

/* ANIMATION ELEMENTS */
.channel-zone {
    position: relative;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.wire {
    position: absolute;
    top: 50%;
    width: 100%;
    height: 2px;
    background: #30363d;
    z-index: -1;
}

.packet {
    position: absolute;
    top: 45%;
    left: 10%; /* Start at arda */
    background: #ffffff;
    color: #000;
    padding: 5px 10px;
    border-radius: 15px;
    font-size: 0.8em;
    opacity: 0; /* Hidden by default */
    box-shadow: 0 0 10px #fff;
}

/* LOGS */
.log-panel {
    margin-top: 30px;
    background: #161b22;
    border: 1px solid #30363d;
    padding: 15px;
    height: 200px;
    overflow-y: auto;
    font-family: monospace;
}
.log-entry { margin: 5px 0; border-bottom: 1px solid #21262d; }
.log-source { font-weight: bold; color: #58a6ff; }
.log-time { color: #8b949e; font-size: 0.8em; margin-right: 10px; }
```

## File: attack_visualizer/templates/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DH Vulnerability Simulator</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>

<div class="header">
    <h1>Diffie-Hellman Protocol <span class="highlight">Attack Lab</span></h1>
    <div class="controls">
        <button onclick="startHandshake('ephemeral')"><i class="fas fa-sync"></i> Ephemeral Handshake (Secure)</button>
        <button onclick="startHandshake('static')"><i class="fas fa-lock"></i> Static Handshake (Risky)</button>
        <button onclick="toggleAttack()" class="btn-red"><i class="fas fa-user-secret"></i> Toggle MitM Attack</button>
        <button onclick="leakKey()" class="btn-warning"><i class="fas fa-radiation"></i> Leak burak's Key</button>
    </div>
</div>

<div class="network-grid">
    <!-- arda -->
    <div class="node" id="node-arda">
        <div class="icon"><i class="fas fa-user-shield"></i></div>
        <h2>arda</h2>
        <div class="status-box">Status: <span id="status-arda">Idle</span></div>
        <div class="key-display" id="key-arda">Shared Secret: ???</div>
    </div>

    <!-- THE CHANNEL (MALLORY) -->
    <div class="channel-zone">
        <div class="wire"></div>
        <div class="packet" id="active-packet"><i class="fas fa-envelope"></i></div>

        <div class="node attacker" id="node-mallory">
            <div class="icon"><i class="fas fa-user-secret"></i></div>
            <h2>Mallory</h2>
            <div class="status-box" id="status-mallory">Mode: Passive</div>
            <div class="hack-console" id="hack-console">Waiting for traffic...</div>
        </div>
    </div>

    <!-- burak -->
    <div class="node" id="node-burak">
        <div class="icon"><i class="fas fa-server"></i></div>
        <h2>burak</h2>
        <div class="status-box">Status: <span id="status-burak">Idle</span></div>
        <div class="key-display" id="key-burak">Shared Secret: ???</div>
    </div>
</div>

<div class="log-panel">
    <h3><i class="fas fa-terminal"></i> Simulation Logs</h3>
    <div id="log-container"></div>
</div>

<script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

## File: attack_visualizer/app.py
```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crypto_engine.protocols import DiffieHellmanProtocol
from benchmark_suite.standard_params import DH_2048_P, DH_2048_G

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Simulation State
STATE = {
    "arda": None,
    "burak": None,
    "mallory_active": False,
    "messages": []
}


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('init_handshake')
def handle_handshake(data):
    """Scenario: Normal DH Handshake"""
    scenario_type = data.get('type')  # 'static' or 'ephemeral'

    # 1. arda Generates Key
    STATE['arda'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
    emit('log', {'source': 'arda', 'msg': f'Generated Private Key: {str(STATE["arda"]._private_key)[:6]}...'})
    emit('anim_key_gen', {'target': 'arda'})

    # 2. burak Generates Key (Static or New)
    if scenario_type == 'static' and STATE['burak']:
        emit('log', {'source': 'burak', 'msg': 'Using STATIC Private Key (No Refresh)'})
    else:
        STATE['burak'] = DiffieHellmanProtocol(DH_2048_P, DH_2048_G)
        emit('log', {'source': 'burak', 'msg': f'Generated Ephemeral Key: {str(STATE["burak"]._private_key)[:6]}...'})
        emit('anim_key_gen', {'target': 'burak'})

    # 3. Public Key Exchange Animation
    emit('anim_packet', {
        'from': 'arda', 'to': 'burak',
        'payload': f'PubA: {str(STATE["arda"].public_key)[:10]}...',
        'intercepted': STATE['mallory_active']
    })


@socketio.on('complete_handshake')
def finalize_handshake():
    """Calculates shared secrets after animation finishes"""
    if STATE['mallory_active']:
        # ATTACK: Subgroup Confinement
        # Mallory injects P-1
        p_minus_1 = DH_2048_P - 1

        # burak computes secret using P-1
        # In a real library this raises an error, here we force it for demo
        # burak's Secret = (P-1)^b mod P
        burak_secret = pow(p_minus_1, STATE['burak']._private_key, DH_2048_P)

        emit('log', {'source': 'Mallory', 'msg': 'ATTACK: Injected (P-1) as Public Key!'})
        emit('log', {'source': 'burak', 'msg': 'Computed Shared Secret (CORRUPTED)'})
        emit('update_status', {'actor': 'burak', 'status': 'compromised', 'secret': str(burak_secret)})
        emit('update_status', {'actor': 'mallory', 'status': 'cracked', 'secret': '1 or P-1'})

    else:
        # Normal DH
        arda_s = STATE['arda'].generate_shared_secret(STATE['burak'].public_key)
        burak_s = STATE['burak'].generate_shared_secret(STATE['arda'].public_key)

        emit('log', {'source': 'System', 'msg': 'Handshake Secure. Channel Established.'})
        emit('update_status', {'actor': 'arda', 'status': 'secure', 'secret': str(arda_s)[:10]})
        emit('update_status', {'actor': 'burak', 'status': 'secure', 'secret': str(burak_s)[:10]})


@socketio.on('toggle_attack')
def toggle_attack():
    STATE['mallory_active'] = not STATE['mallory_active']
    status = "ACTIVE" if STATE['mallory_active'] else "IDLE"
    emit('log', {'source': 'Mallory', 'msg': f'Interception Mode: {status}'})
    emit('update_mallory', {'active': STATE['mallory_active']})


@socketio.on('leak_key')
def leak_key():
    """Forward Secrecy Demo: Leak burak's Key"""
    if not STATE['burak']: return
    key = str(STATE['burak']._private_key)
    emit('log', {'source': 'System', 'msg': f'CRITICAL: burak\'s Key LEAKED: {key[:10]}...'})
    emit('anim_leak', {'key': key})


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)
```

## File: attack_visualizer/requirements.txt
```
flask==3.1.2
flask-socketio==5.5.1
```

## File: benchmark_suite/report_generator.py
```python
import json
import sys
import datetime

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cryptographic Benchmark: DH vs ECDH</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; padding: 20px; background: #f4f4f9; }
        .container { max-width: 1000px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
        .meta { color: #666; font-size: 0.9em; margin-bottom: 20px; }
        .chart-box { margin-bottom: 40px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #007bff; color: white; }
    </style>
</head>
<body>
<div class="container">
    <h1>Diffie-Hellman vs. ECDHE Performance Analysis</h1>
    <div class="meta">Generated on: <span id="date"></span> | Environment: Docker Container</div>

    <div class="chart-box">
        <h3>Execution Time Comparison (Lower is Better)</h3>
        <canvas id="timeChart"></canvas>
    </div>

    <div class="chart-box">
        <h3>Network Payload Efficiency (Lower is Better)</h3>
        <canvas id="sizeChart"></canvas>
    </div>

    <h3>Detailed Data</h3>
    <table id="dataTable">
        <tr><th>Algorithm</th><th>KeyGen (s)</th><th>Handshake (s)</th><th>Payload (Bytes)</th></tr>
    </table>
</div>

<script>
    const data = DATA_PLACEHOLDER;
    document.getElementById('date').innerText = new Date().toLocaleString();

    // Populate Table
    const table = document.getElementById('dataTable');
    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${row.algorithm}</td><td>${row.keygen_avg_sec.toFixed(4)}</td><td>${row.handshake_avg_sec.toFixed(4)}</td><td>${row.payload_bytes}</td>`;
        table.appendChild(tr);
    });

    // Chart 1: Time
    new Chart(document.getElementById('timeChart'), {
        type: 'bar',
        data: {
            labels: data.map(d => d.algorithm),
            datasets: [
                { label: 'Key Generation (s)', data: data.map(d => d.keygen_avg_sec), backgroundColor: '#36a2eb' },
                { label: 'Handshake (s)', data: data.map(d => d.handshake_avg_sec), backgroundColor: '#ff6384' }
            ]
        },
        options: { scales: { y: { beginAtZero: true, title: {display: true, text: 'Seconds'} } } }
    });

    // Chart 2: Size
    new Chart(document.getElementById('sizeChart'), {
        type: 'bar',
        data: {
            labels: data.map(d => d.algorithm),
            datasets: [{ label: 'Public Key Size (Bytes)', data: data.map(d => d.payload_bytes), backgroundColor: '#4bc0c0' }]
        },
        options: { indexAxis: 'y' }
    });
</script>
</body>
</html>
"""


def generate_report(json_data):
    data = json.loads(json_data)
    html_content = HTML_TEMPLATE.replace("DATA_PLACEHOLDER", json.dumps(data))

    filename = "crypto_benchmark_report.html"
    with open(filename, "w") as f:
        f.write(html_content)
    print(f"Report generated: {filename}")


if __name__ == "__main__":
    # Read JSON from stdin
    input_data = sys.stdin.read()
    generate_report(input_data)
```

## File: benchmark_suite/standard_params.py
```python
"""
Bu dosya RFC 3526 (DH) ve NIST (ECDH) standart parametrelerini içerir.
NOT: Hex değerleri okunabilirlik açısından kısaltılmıştır (Placeholder).
Gerçek bir test için bu değerler tam halleriyle değiştirilmelidir.
"""

# --- CLASSIC DH PARAMETERS (RFC 3526) ---

# 2048-bit MODP Group (Group 14)
# P = 2^2048 - 2^1984 - 1 + 2^64 * { [2^1918 pi] + 124476 }
# https://datatracker.ietf.org/doc/html/rfc3526#section-3
DH_2048_P_HEX = """
FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
670C354E 4ABC9804 F1746C08 CA237327 FFFFFFFF FFFFFFFF
"""
DH_2048_P = int(DH_2048_P_HEX.replace(" ", "").replace("\n", ""), 16)
DH_2048_G = 2

# 3072-bit MODP Group (Group 15)
# P = 2^3072 - 2^3008 - 1 + 2^64 * { [2^2942 pi] + 1690314 }
# https://datatracker.ietf.org/doc/html/rfc3526#section-4
DH_3072_P_HEX = """
FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
670C354E 4ABC9804 F1746C08 CA18217C 32905E46 2E36CE3B
E39E772C 180E8603 9B2783A2 EC07A28F B5C55DF0 6F4C52C9
DE2BCBF6 95581718 3995497C EA956AE5 15D22618 98FA0510
15728E5A 8AAAC42D AD33170D 04507A33 A85521AB DF1CBA64
ECFB8504 58DBEF0A 8AEA7157 5D060C7D B3970F85 A6E1E4C7
ABF5AE8C DB0933D7 1E8C94E0 4A25619D CEE3D226 1AD2EE6B
F12FFA06 D98A0864 D8760273 3EC86A64 521F2B18 177B200C
BBE11757 7A615D6C 770988C0 BAD946E2 08E24FA0 74E5AB31
43DB5BFC E0FD108E 4B82D120 A93AD2CA FFFFFFFF FFFFFFFF
"""
# Test amaçlı dummy değer:
DH_3072_P = int(DH_3072_P_HEX.replace(" ", "").replace("\n", ""), 16)
DH_3072_G = 2


# --- ECDH PARAMETERS (NIST) ---

# NIST P-256 (secp256r1)
# https://std.neuromancer.sk/nist/P-256
# y^2 = x^3 - 3x + b (mod p)
NIST_P256_PARAMS = {
    'p': int("0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF", 16),
    'a': int("0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC", 16),
    'b': int("0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B", 16),
    'gx': int("0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296", 16),
    'gy': int("0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5", 16),
    'n': int("0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551", 16)
}

# NIST P-384 (secp384r1)
# https://std.neuromancer.sk/nist/P-384#
# y^2 = x^3 - 3x + b (mod p)
NIST_P384_PARAMS = {
    'p': int("0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff", 16),
    'a': int("0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000fffffffc", 16),
    'b': int("0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef", 16),
    'gx': int("0xaa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf", 16),
    'gy': int("0x3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7", 16),
    'n': int("0xffffffffffffffffffffffffffffffffffffffffffffffffc7634d81f4372ddf581a0db248b0a77aecec196accc52973", 16),
    'h': int("0x1", 16)
}
```

## File: crypto_engine/elliptic_curve.py
```python
from typing import Tuple, Optional

"""
### Teknik Açıklama ("The Why")

Bu kodda uyguladığımız prensipler neden önemli?

1.  **Double-and-Add Algoritması:**
    Tıpkı Klasik DH'deki *Square-and-Multiply* gibi, bu algoritma da işlemin logaritmik zamanda bitmesini sağlar.
    *   256-bitlik bir anahtar (k) için, eğer basit toplama yapsaydık ($P+P+P...$) $2^{256}$ işlem gerekirdi. Bu imkansızdır.
    *   **Double-and-Add** ile sadece yaklaşık **256 tane Point Doubling** ve ortalama **128 tane Point Addition** işlemiyle sonuca ulaşırız. ECDH'yi hızlı ve kullanılabilir kılan budur.

2.  **Modüler Ters (Modular Inverse):**
    Kodda `(y2 - y1) / (x2 - x1)` işlemi yapmamız gerekiyor. Ancak sonlu cisimlerde (Finite Fields) kesirli sayı yoktur.
    *   Örnek: Mod 17'de $4/2 = 2$ dir.
    *   Ancak $4 \times (2^{-1}) \pmod{17}$ olarak hesaplarız.
    *   `_modular_inverse` fonksiyonumuz, Genişletilmiş Öklid algoritmasını kullanarak bu "bölme" işlemini gerçekleştirir. Bu fonksiyon olmadan eğri üzerinde hareket edemezdik.

3.  **Point at Infinity (`None`):**
    Normal sayılarda `0` neyse, Elliptik Eğrilerde "Sonsuzdaki Nokta" odur. Birim elemandır. Kodda bunu `None` olarak temsil ettik ve `point_add` fonksiyonunun başında bu durumu (Identity) özel olarak ele aldık.
"""

# Noktayı temsil etmek için basit bir tip tanımı: (x, y) veya None (Sonsuzdaki Nokta)
Point = Optional[Tuple[int, int]]


class EllipticCurve:
    """
    Weierstrass formundaki elliptik eğriler üzerinde işlemleri gerçekleştirir:
    y^2 = x^3 + ax + b (mod p)

    Kütüphane kullanmadan 'Double-and-Add' algoritmasını uygular.
    """

    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p

    def _modular_inverse(self, n: int) -> int:
        """
        Genişletilmiş Öklid Algoritması (Extended Euclidean Algorithm).
        Mod p'de n'in çarpımsal tersini bulur.
        Yani: (n * x) % p == 1 olan x'i bulur.
        Bu işlem, eğim hesaplarken bölme işlemi yerine kullanılır.
        """
        if n == 0:
            raise ValueError("0'ın tersi yoktur (Sıfıra bölme hatası).")

        n = n % self.p
        original_p = self.p
        x0, x1 = 0, 1

        if self.p == 1: return 0

        temp_n = n
        temp_p = self.p

        while temp_n > 1:
            # Standart öklid algoritması adımları
            q = temp_n // temp_p
            temp_n, temp_p = temp_p, temp_n % temp_p
            x0, x1 = x1 - q * x0, x0

        if x1 < 0:
            x1 += original_p

        return x1

    def point_add(self, P: Point, Q: Point) -> Point:
        """
        İki noktayı toplar: P + Q
        Geometrik olarak: P ve Q'dan geçen doğrunun eğriyi kestiği 3. noktanın x eksenine göre yansıması.
        """
        # 1. Durum: Birim eleman (Sonsuzdaki Nokta - 0) ile toplama
        if P is None: return Q
        if Q is None: return P

        x1, y1 = P
        x2, y2 = Q

        # 2. Durum: Nokta tersi ile toplama (P + (-P) = 0)
        # Dikey bir doğru oluşur, sonsuza gider.
        if x1 == x2 and y1 != y2:
            return None

        # 3. Durum: Nokta kendisiyle toplanıyorsa (P == Q) -> Point Doubling
        if x1 == x2 and y1 == y2:
            return self.point_double(P)

        # 4. Durum: Genel Toplama (P != Q)
        # Eğim (m) = (y2 - y1) / (x2 - x1) mod p
        # Bölme işlemi modüler ters ile çarpmaya dönüşür.
        numerator = (y2 - y1) % self.p
        denominator = (x2 - x1) % self.p

        inv_denom = self._modular_inverse(denominator)
        slope = (numerator * inv_denom) % self.p

        # Yeni koordinatları hesapla
        x3 = (slope * slope - x1 - x2) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def point_double(self, P: Point) -> Point:
        """
        Bir noktayı kendisiyle toplar: P + P = 2P
        Geometrik olarak: P noktasındaki teğetin eğimi kullanılır.
        """
        if P is None: return None

        x1, y1 = P

        # Eğer y1 = 0 ise teğet dikeydir -> Sonsuz
        if y1 == 0:
            return None

        # Eğim (m) = (3x^2 + a) / (2y) mod p
        numerator = (3 * x1 * x1 + self.a) % self.p
        denominator = (2 * y1) % self.p

        inv_denom = self._modular_inverse(denominator)
        slope = (numerator * inv_denom) % self.p

        x3 = (slope * slope - 2 * x1) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def scalar_multiply(self, k: int, P: Point) -> Point:
        """
        Hesaplar: k * P (P noktasını k kere kendisiyle topla)
        Algoritma: Double-and-Add
        Karmaşıklık: O(log k)

        ECDH'de "Public Key" üretimi ve "Shared Secret" hesaplaması burada yapılır.
        k: Private Key (Scalar)
        P: Generator Point
        Sonuç: Public Key (Point)
        """
        result = None  # Başlangıçta 0 (Sonsuzdaki Nokta)
        addend = P

        # Scalar (k) bit bit işlenir
        while k > 0:
            # Eğer son bit 1 ise, mevcut 'addend' değerini sonuca ekle
            if k & 1:
                result = self.point_add(result, addend)

            # Addend'i iki katına çıkar (Double)
            addend = self.point_double(addend)

            # Bir sonraki bite geç
            k >>= 1

        return result
```

## File: crypto_engine/modular_arithmetic.py
```python
import random
"""
### Teknik Açıklama

**Neden `pow()` yerine `square_and_multiply` kullandık?**

Diffie-Hellman güvenliği, Ayrık Logaritma Probleminin (Discrete Logarithm Problem) zorluğuna dayanır: g^a mod p hesaplamak kolaydır, ancak sonuçtan a'yı bulmak zordur.

Eğer a sayısı 2048-bitlik bir sayı ise, değeri yaklaşık 10^617'dir. Eğer bu işlemi "üs kadar çarpma" (naive approach) yaparak hesaplamaya çalışsaydık, evrenin yaşından daha uzun sürerdi.

**Square-and-Multiply**, üssü ikilik tabana çevirerek işlem sayısını sayının bit uzunluğuna (örneğin 2048 adım) indirir.
*   **Örnek:** 3^5 (mod 100)
*   Naive: 3 * 3 * 3 * 3 * 3 (4 çarpma)
*   S&M (5 = 101 binary):
    1.  Bit '1': Kare + Çarp -> 1^2 * 3 = 3
    2.  Bit '0': Kare -> 3^2 = 9
    3.  Bit '1': Kare + Çarp -> 9^2 * 3 = 81 * 3 = 243 ≅ 43 (mod 100)
*   Büyük sayılarda bu fark devasa performans kazancı sağlar ve DH'yi uygulanabilir kılar.
"""

class ModularArithmetic:
    """
    Klasik Diffie-Hellman (DH) için temel matematiksel operasyonları içerir.
    Python'ın built-in pow() fonksiyonunu KULLANMAZ.
    """

    @staticmethod
    def square_and_multiply(base: int, exponent: int, modulus: int) -> int:
        """
        Hesaplar: (base ^ exponent) % modulus
        Algoritma: Square-and-Multiply
        Karmaşıklık: O(log exponent) - Büyük sayılarla çalışmak için zorunludur.
        """
        if modulus == 1:
            return 0

        result = 1
        # Üssü ikilik tabana (binary) çeviriyoruz (örn: 5 -> '101')
        # '0b' öneki olmadan string olarak alıyoruz
        binary_exponent = bin(exponent)[2:]

        for bit in binary_exponent:
            # Adım 1: Square (Kare Al)
            result = (result * result) % modulus

            # Adım 2: Multiply (Eğer bit 1 ise Çarp)
            if bit == '1':
                result = (result * base) % modulus

        return result

    @staticmethod
    def generate_prime_candidate(length: int) -> int:
        """
        Basit bir test amaçlı asal sayı adayı üretir (Miller-Rabin testi eklenebilir).
        Bu simülasyon için random büyük tek sayılar üretiyoruz.
        """
        p = random.getrandbits(length)
        # Sayının tek sayı olduğundan ve en yüksek bitin 1 olduğundan emin ol
        p |= (1 << length - 1) | 1
        return p

    @staticmethod
    def is_prime(n: int, k: int = 5) -> bool:
        """
        Miller-Rabin asallık testi.
        Büyük sayıların asallığını olasılıksal olarak test eder.
        """
        if n == 2 or n == 3: return True
        if n % 2 == 0: return False

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = ModularArithmetic.square_and_multiply(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = ModularArithmetic.square_and_multiply(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    @staticmethod
    def get_safe_prime(length: int) -> int:
        """
        Belirtilen bit uzunluğunda bir asal sayı döndürür.
        Gerçek dünya senaryosu için RFC 3526 grupları kullanılmalıdır,
        ancak burada matematiksel motoru test ediyoruz.
        """
        while True:
            p = ModularArithmetic.generate_prime_candidate(length)
            if ModularArithmetic.is_prime(p):
                return p
```

## File: .gitignore
```
# add default ignores for python projects
__pycache__/
*.py[cod]
.env/
*.pyo
*.pyd


# add ignores for common IDEs
.vscode/
.idea/

# add ignores for macOS
.DS_Store

# Custom
Implementation-Plan-Task-Lists.md
references/
repomix.config.json
```

## File: crypto_benchmark_report.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Cryptographic Benchmark: DH vs ECDH</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; padding: 20px; background: #f4f4f9; }
        .container { max-width: 1000px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
        .meta { color: #666; font-size: 0.9em; margin-bottom: 20px; }
        .chart-box { margin-bottom: 40px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #007bff; color: white; }
    </style>
</head>
<body>
<div class="container">
    <h1>Diffie-Hellman vs. ECDHE Performance Analysis</h1>
    <div class="meta">Generated on: <span id="date"></span> | Environment: Docker Container</div>

    <div class="chart-box">
        <h3>Execution Time Comparison (Lower is Better)</h3>
        <canvas id="timeChart"></canvas>
    </div>

    <div class="chart-box">
        <h3>Network Payload Efficiency (Lower is Better)</h3>
        <canvas id="sizeChart"></canvas>
    </div>

    <h3>Detailed Data</h3>
    <table id="dataTable">
        <tr><th>Algorithm</th><th>KeyGen (s)</th><th>Handshake (s)</th><th>Payload (Bytes)</th></tr>
    </table>
</div>

<script>
    const data = [{"algorithm": "DH-2048", "keygen_avg_sec": 0.025766837593982926, "keygen_std_sec": 0.024113325376813658, "handshake_avg_sec": 0.03153084580262657, "handshake_std_sec": 0.02352587616812542, "payload_bytes": 256}, {"algorithm": "ECDH-256", "keygen_avg_sec": 0.022557516896631567, "keygen_std_sec": 0.0219389698738718, "handshake_avg_sec": 0.026570795802399516, "handshake_std_sec": 0.023815311897021244, "payload_bytes": 64}, {"algorithm": "DH-3072", "keygen_avg_sec": 0.1626172375981696, "keygen_std_sec": 0.025811362160904343, "handshake_avg_sec": 0.25979893340554555, "handshake_std_sec": 0.02675821462616564, "payload_bytes": 384}];
    document.getElementById('date').innerText = new Date().toLocaleString();

    // Populate Table
    const table = document.getElementById('dataTable');
    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${row.algorithm}</td><td>${row.keygen_avg_sec.toFixed(4)}</td><td>${row.handshake_avg_sec.toFixed(4)}</td><td>${row.payload_bytes}</td>`;
        table.appendChild(tr);
    });

    // Chart 1: Time
    new Chart(document.getElementById('timeChart'), {
        type: 'bar',
        data: {
            labels: data.map(d => d.algorithm),
            datasets: [
                { label: 'Key Generation (s)', data: data.map(d => d.keygen_avg_sec), backgroundColor: '#36a2eb' },
                { label: 'Handshake (s)', data: data.map(d => d.handshake_avg_sec), backgroundColor: '#ff6384' }
            ]
        },
        options: { scales: { y: { beginAtZero: true, title: {display: true, text: 'Seconds'} } } }
    });

    // Chart 2: Size
    new Chart(document.getElementById('sizeChart'), {
        type: 'bar',
        data: {
            labels: data.map(d => d.algorithm),
            datasets: [{ label: 'Public Key Size (Bytes)', data: data.map(d => d.payload_bytes), backgroundColor: '#4bc0c0' }]
        },
        options: { indexAxis: 'y' }
    });
</script>
</body>
</html>
```

## File: Dockerfile
```dockerfile
# Base image: Python 3.9 (Slim version for lighter footprint)
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Kodları konteynera kopyala
COPY crypto_engine /app/crypto_engine
COPY benchmark_suite /app/benchmark_suite
# (İleride attack_lab de eklenecek)

# Bağımlılık yok (No pip install needed for pure math implementation!)
# Ancak ileride grafik çizmek gerekirse matplotlib eklenebilir.

# Benchmark scriptini çalıştır
CMD ["python", "-m", "benchmark_suite.benchmark"]
```

## File: benchmark_suite/benchmark.py
```python
# File: benchmark_suite/benchmark.py
import time
import sys
import os
import json
import statistics

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_engine.protocols import DiffieHellmanProtocol, ECDHProtocol
from crypto_engine.elliptic_curve import EllipticCurve
import benchmark_suite.standard_params as params


def measure_execution(func, iterations=10):
    """Executes a function multiple times and returns mean and stdev."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append(end - start)

    return statistics.mean(times), statistics.stdev(times)


def run_suite():
    results = []

    print("--- Başlatılıyor: Kriptografik Performans Ölçümü ---", file=sys.stderr)

    # --- Test 1: DH-2048 (Group 14) ---
    def dh_2048_keygen():
        return DiffieHellmanProtocol(params.DH_2048_P, params.DH_2048_G)

    # Pre-generate arda for Handshake test
    arda_dh_2048 = dh_2048_keygen()
    burak_dh_2048_pub = dh_2048_keygen().public_key

    def dh_2048_handshake():
        arda_dh_2048.generate_shared_secret(burak_dh_2048_pub)

    # --- Test 2: ECDH-256 (NIST P-256) ---
    # Equivalent to 3072-bit RSA/DH security (approx 128-bit security level)
    curve_256 = EllipticCurve(params.NIST_P256_PARAMS['a'], params.NIST_P256_PARAMS['b'], params.NIST_P256_PARAMS['p'])
    G_256 = (params.NIST_P256_PARAMS['gx'], params.NIST_P256_PARAMS['gy'])
    n_256 = params.NIST_P256_PARAMS['n']

    def ecdh_256_keygen():
        return ECDHProtocol(curve_256, G_256, n_256)

    arda_ecdh_256 = ecdh_256_keygen()
    burak_ecdh_256_pub = ecdh_256_keygen().public_key

    def ecdh_256_handshake():
        arda_ecdh_256.generate_shared_secret(burak_ecdh_256_pub)

    # --- Test 3: DH-3072 (Group 15) ---
    def dh_3072_keygen():
        return DiffieHellmanProtocol(params.DH_3072_P, params.DH_3072_G)

    arda_dh_3072 = dh_3072_keygen()
    burak_dh_3072_pub = dh_3072_keygen().public_key

    def dh_3072_handshake():
        arda_dh_3072.generate_shared_secret(burak_dh_3072_pub)

    # --- Execution & Collection ---
    scenarios = [
        ("DH-2048", dh_2048_keygen, dh_2048_handshake, 2048 / 8),
        ("ECDH-256", ecdh_256_keygen, ecdh_256_handshake, 256 / 8 * 2),  # Approx point size
        ("DH-3072", dh_3072_keygen, dh_3072_handshake, 3072 / 8),
    ]

    for name, keygen_func, handshake_func, size_bytes in scenarios:
        print(f"Benchmarking {name}...", file=sys.stderr)
        kg_mean, kg_std = measure_execution(keygen_func)
        hs_mean, hs_std = measure_execution(handshake_func)

        results.append({
            "algorithm": name,
            "keygen_avg_sec": kg_mean,
            "keygen_std_sec": kg_std,
            "handshake_avg_sec": hs_mean,
            "handshake_std_sec": hs_std,
            "payload_bytes": int(size_bytes)
        })

    # Dump JSON to stdout for piping
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    run_suite()
```

## File: crypto_engine/protocols.py
```python
import secrets
from typing import Optional, Tuple
from .modular_arithmetic import ModularArithmetic
from .elliptic_curve import EllipticCurve, Point

"""
### Teknik Açıklama ("The Why")

1.  **Ephemeral vs. Static:**
    *   Sınıflarımızda `private_key` parametresi opsiyoneldir.
    *   Eğer boş bırakılırsa (`None`), `secrets.randbelow()` kullanılarak her seferinde yeni bir anahtar üretilir. Bu **Ephemeral (Geçici)** anahtar değişimidir ve **Forward Secrecy (İleriye Dönük Gizlilik)** sağlar. Yani bir saldırgan gelecekte sunucuyu hacklese bile, geçmişte üretilen bu rastgele anahtarları bulamaz (çünkü silinmiştir).
    *   Eğer bir `private_key` verilirse, bu **Static** anahtar değişimidir. 3. Aşamada (Break Phase), statik anahtar kullanan bir sistemin geçmiş mesajlarının nasıl çözüldüğünü göstereceğiz.

2.  **Güvenlik Kontrolleri:**
    *   `DiffieHellmanProtocol` içinde `if other_public_key <= 1...` kontrolü ekledik. Bu, **Small Subgroup Confinement Attack** (Küçük Alt Grup Hapsetme Saldırısı) önlemidir. Saldırganın araya girip `1` veya `p-1` göndererek ortak sırrı tahmin edilebilir (1 veya -1) hale getirmesini engeller.
    *   3. Aşamada "Saf burak" (Naive burak) karakterini yaratırken bu kontrolleri bilerek kaldıracağız.

3.  **Performans Farkı (Teorik):**
    *   `DiffieHellmanProtocol` public key üretmek için 2048-bitlik bir üs alma işlemi yapar (`square_and_multiply`).
    *   `ECDHProtocol` ise 256-bitlik bir skaler çarpım yapar (`scalar_multiply`).
    *   Bir sonraki aşamada (Measure Phase), bu bit farkının (2048 vs 256) işlemci sürelerine nasıl yansıdığını ölçeceğiz.
"""

class DiffieHellmanProtocol:
    """
    Klasik Diffie-Hellman (DH) Protokolü.
    Hem Ephemeral (DHE) hem de Static DH senaryolarını destekler.
    """

    def __init__(self, p: int, g: int, private_key: Optional[int] = None):
        """
        :param p: Asal modül (Prime modulus)
        :param g: Üreteç (Generator)
        :param private_key: Eğer verilirse 'Static DH' olur, verilmezse rastgele üretilir (Ephemeral).
        """
        self.p = p
        self.g = g

        # Eğer özel anahtar verilmediyse, kriptografik olarak güvenli rastgele bir sayı üret (Ephemeral)
        # Aralık: [2, p-2]
        if private_key is None:
            self._private_key = 2 + secrets.randbelow(p - 3)
            self.is_ephemeral = True
        else:
            self._private_key = private_key
            self.is_ephemeral = False

        # Public Key Hesaplama: A = g^a mod p
        # Kendi yazdığımız Square-and-Multiply algoritmasını kullanıyoruz.
        self.public_key = ModularArithmetic.square_and_multiply(self.g, self._private_key, self.p)

    def generate_shared_secret(self, other_public_key: int) -> int:
        """
        Karşı tarafın Public Key'ini (B) kullanarak ortak sırrı hesaplar.
        S = B^a mod p
        """
        # Güvenlik Kontrolü: Gelen anahtarın 1 veya p-1 olup olmadığı kontrol edilmeli (Small Subgroup Attack)
        # Ancak "Break" aşamasında bu kontrolü bilerek yapmayan "Naive burak" kullanacağız.
        # Bu sınıf güvenli versiyonu temsil etsin:
        if other_public_key <= 1 or other_public_key >= self.p - 1:
            raise ValueError("Gecersiz Public Key! (Small Subgroup Saldirisi Riski)")

        shared_secret = ModularArithmetic.square_and_multiply(other_public_key, self._private_key, self.p)
        return shared_secret


class ECDHProtocol:
    """
    Elliptic Curve Diffie-Hellman (ECDH) Protokolü.
    Daha küçük anahtar boyutlarıyla aynı güvenlik seviyesini sağlar.
    """

    def __init__(self, curve: EllipticCurve, G: Point, order_n: int, private_key: Optional[int] = None):
        """
        :param curve: EllipticCurve sınıfı örneği (y^2 = x^3 + ax + b)
        :param G: Başlangıç noktası (Generator Point)
        :param order_n: G noktasının mertebesi (Order of subgroup)
        :param private_key: Opsiyonel statik anahtar.
        """
        self.curve = curve
        self.G = G
        self.n = order_n

        # Private Key (d): [1, n-1] aralığında rastgele bir tam sayı
        if private_key is None:
            self._private_key = 1 + secrets.randbelow(self.n - 1)
            self.is_ephemeral = True
        else:
            self._private_key = private_key
            self.is_ephemeral = False

        # Public Key (Q): Q = d * G
        # Kendi yazdığımız Double-and-Add algoritmasını kullanıyoruz.
        self.public_key = self.curve.scalar_multiply(self._private_key, self.G)

    def generate_shared_secret(self, other_public_key: Point) -> int:
        """
        Karşı tarafın Public Key'ini (Q_other) kullanarak ortak sırrı hesaplar.
        S_point = d * Q_other
        Shared Secret = S_point.x (Sadece x koordinatı kullanılır)
        """
        if other_public_key is None:
            raise ValueError("Gecersiz Public Key (Sonsuzdaki Nokta)!")

        # S = d * Q_other
        shared_point = self.curve.scalar_multiply(self._private_key, other_public_key)

        if shared_point is None:
            raise ValueError("Ortak sır Sonsuzdaki Nokta çıktı! (Kritik Hata)")

        # ECDH standartlarında genellikle sonucun x koordinatı ortak sır olarak alınır.
        return shared_point[0]
```

## File: Makefile
```
.PHONY: build benchmark-iot benchmark-server

build:
	@echo "Building Crypto Workbench..."
	docker build -t crypto-bench .

# Runs benchmark inside limited container, pipes JSON to local report generator
benchmark-iot:
	@echo "Running Simulation: IoT / Ad-Hoc Network Node (Low CPU)..."
	docker run --rm --cpus="0.5" --memory="128m" crypto-bench python -m benchmark_suite.benchmark | python3 benchmark_suite/report_generator.py
	@echo "Opening Report..."
	# Linux/Mac için open/xdg-open, Windows için start kullanılabilir
	# open crypto_benchmark_report.html

benchmark-server:
	@echo "Running Simulation: High Performance Server..."
	docker run --rm --cpus="2.0" --memory="1g" crypto-bench python -m benchmark_suite.benchmark | python3 benchmark_suite/report_generator.py
```
