# Tiny-Agent Reliability: 4-bit vs 8-bit CPU Quant

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-reliability-4-bit-vs-8-bit-cpu-quant-6f57fd2d87fa`
Run ID: `tiny-agent-reliability-4-bit-vs-8-bit-cpu-quant-6f57fd2d87fa-20260611T104558739796+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb94e1342f57

## What looked useful

With a competent float baseline over 5 seeds and 350 held-out episodes per seed, float and int8 both reached 0.997714 mean episode success, while int4 reached 0.933143; int4 lost only 0.002168 absolute action accuracy but 0.064571 absolute episode success.

## Boundaries and scale limits

Toy no-obstacle gridworld only; not an LLM/tool agent, not actual int4/int8 CPU kernels, no activation quantization, no production serving stack, and obstacle-rich variants did not have a competent float baseline.

## Claim scope

In a reproducible NumPy toy gridworld policy with weight-only symmetric per-channel quantization and fp32 dequantized CPU inference, 4-bit quantization caused a small action-accuracy loss that amplified into a larger closed-loop episode-success loss, while 8-bit matched float.

## Why it stopped

Finalize as no-paper useful signal: the result supports the mechanism in a toy/proxy setting but is not direct or broad enough for publication-grade validation.

## Recommended next action

Run a bounded direct follow-up on a real tiny language-model or tool-use agent with actual CPU int4/int8 inference kernels, using closed-loop task success as the primary metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Closed-loop reliability of real tiny agents under CPU int4 vs int8 inference
- Success threshold: Across at least 3 seeds or model initializations, int4 shows a materially larger closed-loop success drop than int8, and the closed-loop drop is at least 3x the static metric drop in relative terms.
- Stop condition: Stop as negative if float/int8/int4 closed-loop success differ by less than 1 absolute percentage point or if the float baseline cannot exceed 90% task success on the chosen tasks.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-reliability-4-bit-vs-8-bit-cpu-quant-6f57fd2d87fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
