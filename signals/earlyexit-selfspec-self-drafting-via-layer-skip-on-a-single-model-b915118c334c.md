# EarlyExit-SelfSpec: Self-Drafting via Layer Skip on a Single Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `earlyexit-selfspec-self-drafting-via-layer-skip-on-a-single-model-b915118c334c`
Run ID: `earlyexit-selfspec-self-drafting-via-layer-skip-on-a-single-model-b915118c334c-20260609T130551393947+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7332396d4975

## What looked useful

Prefix early exits accepted at most 1.124 tokens per 4-token cycle at 11/12 layers versus a 4.667-token idealized break-even threshold. The best skipped-block draft, even6, accepted 0.534 tokens per 4-token cycle versus a 3.000-token threshold. Raw layer skipping improved over same-depth prefix exits but remained far from viable.

## Boundaries and scale limits

Evidence is limited to GPT-2 small, Wikitext-2 validation, greedy argmax acceptance, no trained auxiliary heads, no KV-cache reuse implementation, and no larger-model or sampling-based serving benchmark.

## Claim scope

On GPT-2 small with Wikitext-2 validation prefixes, untrained early-exit and skipped-block draft paths using the original final layer norm and LM head do not match the full model often enough for greedy self-speculative decoding to plausibly speed up under an idealized gamma=4 cost model.

## Why it stopped

Proxy early falsification: direct greedy agreement and acceptance on a GPT-2-small-class model are far below even an optimistic speedup threshold, so a full serving implementation is not justified for the untrained variant.

## Recommended next action

Stop this raw untrained draft-path variant; if continuing, run a bounded follow-up that trains lightweight early-exit or skipped-block draft heads and requires gamma=4 accepted tokens per cycle to exceed implemented latency break-even.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for single-model self-spec drafting
- Success threshold: At gamma=4, the trained draft path must exceed the measured implemented latency break-even and deliver at least 1.15x wall-clock tokens/sec over dense greedy decoding on the same hardware and validation prompts.
- Stop condition: Stop if trained heads fail to double raw accepted tokens per cycle or if the actual speculative loop is slower than dense decoding after a bounded training run.

## Evidence references

- Artifact root: `<local-path>/projects/earlyexit-selfspec-self-drafting-via-layer-skip-on-a-single-model-b915118c334c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
