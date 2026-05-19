# Cross-Model KV-Cascade Router with Affine Adapter

Status: `useful_signal`
Project ID: `cross-model-kv-cascade-router-with-affine-adapter-64f380dca440`
Run ID: `cross-model-kv-cascade-router-with-affine-adapter-64f380dca440-20260517T231253219085+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b29b30c8532f

## What looked useful

Adapted source KV improved over destructive controls: CE 2.163 versus zero 2.743 and random 3.047, KV MSE 1.147 versus zero 2.369 and random 4.739. But target CE was 0.817, so adapted-cache substitution caused a large +1.347 CE delta.

## Boundaries and scale limits

Synthetic deterministic language only; independently trained toy models only; no pretrained model pair, no GPT-2-class baseline, no real serving router, no latency benchmark, no long autoregressive rollout.

## Claim scope

In a two-layer synthetic-language transformer pair with 32-dim source and 48-dim target states, learned per-layer affine K/V maps recover nontrivial target-KV structure versus zero/random controls but do not preserve target next-token behavior well enough for cache substitution.

## Why it stopped

Early bounded falsification of the simple affine-cache substitution claim: the adapter beats zero/random proxy controls but fails the direct preservation threshold by a large margin, so this is not full validation.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded deepen test adding a cheap residual KV calibrator and acceptance router on the same harness before any larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Calibrated KV Adapter with Acceptance Router
- Success threshold: Accepted adapted-cache cases achieve mean CE delta <= 0.05 versus target at >= 30% token/sequence acceptance, and outperform affine-only on all reported seeds.
- Stop condition: Stop if residual calibration cannot reach CE delta <= 0.05 at >= 30% acceptance on at least two of three seeds, or if the router requires target-model computation that eliminates cascade savings.

## Evidence references

- Artifact root: `<local-path>/projects/cross-model-kv-cascade-router-with-affine-adapter-64f380dca440`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
