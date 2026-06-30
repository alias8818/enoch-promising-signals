# Token-Tree CPU Self-Speculation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `token-tree-cpu-self-speculation-e7c43937f478`
Run ID: `token-tree-cpu-self-speculation-e7c43937f478-20260522T181506583183+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acbb5f2d3255

## What looked useful

Across 27 logged conditions, no branch>1 token-tree case beat baseline. The best branching case was 0.811x baseline despite 99% draft-hit and 8-thread verification; branch=1 linear speculation only reached break-even under 99% draft-hit.

## Boundaries and scale limits

Not a real transformer or LLM-serving benchmark; does not model KV-cache reuse, learned self-draft heads, tokenizer/prompt distributions, or optimized batched transformer kernels. Vocab was 4096 and generation length was 4096 tokens per condition.

## Claim scope

In a bounded CPU Markov-language-model proxy with dense per-token target argmax, synthetic draft-hit controls, branch factors 1/2/4, depths 2/4, and up to 8-thread parallel tree verification, token-tree branching did not improve greedy decoding wall-clock throughput.

## Why it stopped

Proxy CPU evidence was negative for token-tree branching rather than full validation: extra target evaluations for unused branches outweighed accepted-token gains in all branching conditions tested.

## Recommended next action

Stop this run as a proxy early falsification; only reopen with a bounded real-transformer CPU test that demonstrates batched verification can overcome extra branch evaluations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer CPU Token-Tree Verification
- Success threshold: Branch=2 depth<=4 token-tree decoding achieves at least 1.15x greedy wall-clock throughput and beats branch=1 linear speculation by at least 5% at matched output tokens on CPU.
- Stop condition: Stop if branch=2 remains below 1.0x greedy or fails to beat branch=1 linear speculation after the tiny-transformer implementation and 50-context benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/token-tree-cpu-self-speculation-e7c43937f478`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
