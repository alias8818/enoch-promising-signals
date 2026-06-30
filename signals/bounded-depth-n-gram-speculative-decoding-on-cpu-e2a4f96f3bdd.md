# Bounded-Depth N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-depth-n-gram-speculative-decoding-on-cpu-e2a4f96f3bdd`
Run ID: `bounded-depth-n-gram-speculative-decoding-on-cpu-e2a4f96f3bdd-20260608T165313463555+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fc88751159c5

## What looked useful

The mechanism works when continuations repeat strongly, but exact bounded-depth n-gram drafting is too sparse and low-acceptance on the tested natural-text trace to produce meaningful CPU target-call savings.

## Boundaries and scale limits

No transformer target model, no real CPU LLM runtime, no KV-cache measurement, no prompt-suite serving benchmark, and no quality-equivalence test. Results are trace/proxy evidence only and cannot support a publication-grade LLM serving claim.

## Claim scope

Single-process CPU proxy experiments for bounded-depth n-gram speculative decoding using a held-out Tiny Shakespeare word-token trace plus a repetitive synthetic control. The natural-text trace showed at most 2.63% target-call reduction and no reliable proxy wall-clock speedup; the repetitive synthetic control showed up to 70.61% target-call reduction and 3.45x proxy speedup.

## Why it stopped

Proxy early falsification for natural-text CPU usefulness: best real-text target-call reduction was only 2.63% and best meaningful speculative wall-clock row was break-even, although a synthetic repetitive control verified the mechanism.

## Recommended next action

Stop this run as a no-paper useful signal; the only worthwhile bounded next test is direct integration with a real CPU LLM runtime and a >=10% end-to-end tokens/sec success threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM n-gram speculative decoding benchmark
- Success threshold: At least 10% end-to-end CPU tokens/sec improvement over baseline on a representative prompt suite, with no measurable output-quality regression and target-call reduction large enough to exceed drafter overhead.
- Stop condition: Stop if target-call reduction remains below 5% or end-to-end tokens/sec improvement remains below 5% on two representative prompt domains after adaptive depth/context tuning.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-depth-n-gram-speculative-decoding-on-cpu-e2a4f96f3bdd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
