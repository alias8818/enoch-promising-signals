# Bounded Suffix-Trie CPU Draft Decoder

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `bounded-suffix-trie-cpu-draft-decoder-7cbb1351d55e`
Run ID: `bounded-suffix-trie-cpu-draft-decoder-7cbb1351d55e-20260609T174045207768+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/39c5b43f8902

## What looked useful

The trie mechanism works narrowly but is not compelling as a standalone CPU draft decoder: it won by only 2.1% relative over fixed lookup on Tiny Shakespeare, lost by 2.7% relative on Alice, used much larger structures, and had slower mean lookup.

## Boundaries and scale limits

No real CPU language model integration, no BPE tokenizer, no target logits, no batched verification, no KV-cache or sampling effects, and only two small public text corpora with 20k train and 10k eval tokens each.

## Claim scope

In a bounded oracle-token benchmark over two public prose corpora, a bounded suffix-trie can reduce simulated target calls versus no drafter, but it does not reliably beat simple fixed-order lookup under comparable CPU cost and memory.

## Why it stopped

Proxy evidence is useful but does not support the bounded suffix-trie over simpler fixed-order lookup; this is not full validation of CPU speculative decoding.

## Recommended next action

Stop this trie-only line unless a real CPU LM trace shows fixed bigram or prompt-lookup baselines leave large repeat spans unexploited.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/bounded-suffix-trie-cpu-draft-decoder-7cbb1351d55e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
