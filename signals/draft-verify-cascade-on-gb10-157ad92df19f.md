# Draft-Verify Cascade on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `draft-verify-cascade-on-gb10-157ad92df19f`
Run ID: `draft-verify-cascade-on-gb10-157ad92df19f-20260611T211901827707+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3da898a765a2

## What looked useful

Best tested assistant-token budget was 16, with 56.827 mean wall tokens/s versus 51.916 for verifier-only baseline (1.095x). However, every assistant-token budget diverged from verifier-only greedy output on 2/4 prompts, and a repeatability check showed deterministic non-equivalence.

## Boundaries and scale limits

Four prompts, 64 generated tokens each, one target/assistant model pair, greedy decoding only, Transformers generate assistant_model path only; not a production-serving, vLLM/SGLang, 7B+, sampling, or quality benchmark.

## Claim scope

On one NVIDIA GB10 using cached Qwen/Qwen2.5-0.5B as assistant and Qwen/Qwen2.5-1.5B as verifier through Transformers assisted generation, the local draft-verify path produced a small throughput gain but did not preserve verifier-only greedy token IDs on all prompts.

## Why it stopped

Early local falsification of the exact draft-verify cascade criterion: the tested path showed only a modest speedup and failed exact verifier-only greedy output preservation.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit with an implementation/backend that first proves exact verifier-equivalent greedy decoding before scaling throughput tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact KV-Aware Draft-Verify Control on GB10
- Success threshold: All prompts must match verifier-only greedy token IDs exactly and mean wall throughput must be at least 1.25x the verifier-only baseline.
- Stop condition: Stop immediately as negative if exact token-ID equivalence fails on any prompt after implementation bugs are ruled out, or if mean speedup remains below 1.10x after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/draft-verify-cascade-on-gb10-157ad92df19f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
