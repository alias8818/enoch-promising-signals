# CPU Federated Toy: Cheating-Resistant Gradient Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-federated-toy-cheating-resistant-gradient-verification-780e3cac6cd1`
Run ID: `cpu-federated-toy-cheating-resistant-gradient-verification-780e3cac6cd1-20260613T140231976115+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f83ebaa4f43d

## What looked useful

Large audits detected broad nonadaptive sign-flip and Gaussian-noise attacks with about 0.88-0.90 best mean detection across three seeds, but zero-gradient and scale attacks stayed weak at about 0.18 and 0.38 best mean detection, and a known-projection adaptive attack stayed near the 0.01 false-positive target. This falsifies the toy protocol as a robust cheating-resistant gradient verifier.

## Boundaries and scale limits

No privacy-preserving commitment scheme, secure transcript, real FL workload, non-IID benchmark, neural-network gradient, or cryptographic proof was tested. The strongest detection required auditing 64 of 128 local examples, which is likely too costly for the intended cheating-resistant FL setting.

## Claim scope

CPU toy simulation of probabilistic spot-audit verification for 20D logistic-regression client gradients with 128 examples/client, calibrated honest-client threshold at target FPR 0.01, and three full seeds.

## Why it stopped

Proxy/toy early falsification: the tested spot-audit verifier does not robustly detect important cheating modes under bounded local evidence, so it is not ready for paper claims.

## Recommended next action

Stop this protocol as no-paper evidence; a next bounded test should add challenge-after-commitment transcript enforcement plus a stronger consistency statistic for zero/scale cheating before considering larger FL workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Challenge-After-Commitment Gradient Audits With Stronger Zero/Scale Detection
- Success threshold: Across three seeds, zero, scale, and adaptive attacks each achieve mean detection rate >= 0.8 at target FPR 0.01 with audit_k <= 32/128 and no challenge leakage.
- Stop condition: Stop if zero or scale attack detection remains below 0.5 at k=32 and target FPR 0.01 after adding commitment timing and the stronger statistic.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-federated-toy-cheating-resistant-gradient-verification-780e3cac6cd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
