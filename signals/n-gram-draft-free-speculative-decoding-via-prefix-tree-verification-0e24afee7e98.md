# n-gram draft-free speculative decoding via prefix-tree verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-free-speculative-decoding-via-prefix-tree-verification-0e24afee7e98`
Run ID: `n-gram-draft-free-speculative-decoding-via-prefix-tree-verification-0e24afee7e98-20260611T222954959359+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/441f70712620

## What looked useful

Across 128 paired trials of 128 generated tokens, branch-8 prefix-tree verification improved the latency proxy from 6.185x to 7.118x over autoregressive decoding and beat linear retrieval in 100/128 trials, but required 4.269x the verified-node compute of linear retrieval. Branch 2-4 looked like the best tradeoff.

## Boundaries and scale limits

No real transformer, tokenizer, GPU tree attention mask, KV-cache behavior, sampling-correct verification, or production serving stack was tested. Results are a local mechanism proxy over one small public corpus.

## Claim scope

In a deterministic word n-gram target-LM proxy on Tiny Shakespeare, draft-free n-gram retrieval merged into a prefix tree reduces target verification passes versus single-continuation retrieval, but the gain is modest and comes with substantially higher verified-node compute.

## Why it stopped

This run produced a useful proxy signal but not direct publication-grade evidence; existing public work already covers related training-free retrieval and tree-verification ideas.

## Recommended next action

Run a bounded real-LM timing follow-up with GPT-2-small-class or similar local model, actual tree-mask verification, greedy exact-output checks, and branch limits 2-4 before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM timing test for small-branch n-gram prefix-tree verification
- Success threshold: Branch-2 or branch-4 tree verification achieves at least 1.10x wall-clock throughput over linear n-gram retrieval and at least 1.50x over autoregressive decoding on 100+ prompts, with exact greedy-output equivalence and less than 2.5x verified-node overhead versus linear retrieval.
- Stop condition: Stop if tree-mask overhead makes branch-2/4 slower than linear retrieval, if exact greedy-output equivalence fails, or if acceptance gains disappear outside highly repetitive prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-free-speculative-decoding-via-prefix-tree-verification-0e24afee7e98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
