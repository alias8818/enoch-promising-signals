# N-Gram CPU Draft Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-draft-speculative-decoding-fd662ff37d30`
Run ID: `n-gram-cpu-draft-speculative-decoding-fd662ff37d30-20260522T180118976978+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e584580b701c

## What looked useful

Best prose upper bounds were only 1.40-1.51 ideal target tokens per call, while Python stdlib code reached 4.22 and synthetic repetition reached 15.87; p99 lookup cost stayed below 1 microsecond in the Python prototype.

## Boundaries and scale limits

Evaluated on 44k-120k token local/proxy corpora with no target model forward pass, no GPU wall-clock speculative decoding integration, no production traces, and no comparison to learned draft models.

## Claim scope

Online CPU n-gram drafting over GPT-2-token streams can cheaply propose exact future tokens for repeated/code-like text, but provides only weak target-call reduction upper bounds on ordinary prose in this local benchmark.

## Why it stopped

Bounded proxy evidence supports a workload-specific mechanism but not a publication-grade or general speculative-decoding claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded end-to-end small-LM speculative decoding test on code/document-continuation prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU n-gram speculative decoding on a small causal LM
- Success threshold: At least 1.25x end-to-end tokens/second speedup on code/document-continuation prompts with no slowdown greater than 5% on prose controls.
- Stop condition: Stop if target-model integration shows less than 1.10x speedup on code/document prompts or if CPU/index overhead erases the target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-draft-speculative-decoding-fd662ff37d30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
