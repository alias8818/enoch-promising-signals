# Speculative cascade: n-gram draft + small LM verifier vs single large LM on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-cascade-n-gram-draft-small-lm-verifier-vs-single-large-lm-on-cpu-2370663274c3`
Run ID: `speculative-cascade-n-gram-draft-small-lm-verifier-vs-single-large-lm-on-cpu-2370663274c3-20260610T121521827950+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7b7f6e596e3d

## What looked useful

distilgpt2 cascade preserved some gpt2 behavior but reached only 1.44x generation speedup; the n-gram accepted tokens reduced large-model agreement compared with the small verifier alone. tiny-gpt2 delivered high speed but 0% teacher agreement and 0% held-out top-1 accuracy in the sampled probe.

## Boundaries and scale limits

Does not test modern 7B+ LMs, quantized serving runtimes, batching, non-Wikitext prompt distributions, human evaluation, or true speculative decoding with large-model verification.

## Claim scope

Bounded CPU proxy using Wikitext-2, GPT-2 tokenization, n-gram draft proposals, distilgpt2 or sshleifer/tiny-gpt2 as the small verifier, and gpt2 as the large baseline.

## Why it stopped

Proxy early falsification: the behavior-preserving verifier missed the speed threshold, while the fast verifier failed the quality threshold; this is not a full modern-LLM validation.

## Recommended next action

Stop treating the unoptimized n-gram plus small-verifier cascade as viable versus a single gpt2 CPU baseline; only run a bounded follow-up if testing quantized/optimized distilgpt2-class verification against the same 2x speed and quality thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantized distilgpt2 verifier threshold ablation for CPU cascade
- Success threshold: At least 2x cascade generation speedup versus gpt2 and at least 60% teacher-forced top-1 agreement with gpt2, without dropping held-out top-1 accuracy more than 25% relative to gpt2.
- Stop condition: Stop if no threshold reaches both 2x speedup and the agreement/accuracy thresholds, or if n-gram accepted tokens still reduce agreement relative to the small verifier alone.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-cascade-n-gram-draft-small-lm-verifier-vs-single-large-lm-on-cpu-2370663274c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
