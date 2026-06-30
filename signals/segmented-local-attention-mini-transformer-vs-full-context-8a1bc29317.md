# Segmented local-attention mini-Transformer vs full-context mini-GPT on BPE WikiText

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `33`
Project ID: `segmented-local-attention-mini-transformer-vs-full-context-8a1bc29317`
Run ID: `segmented-local-attention-mini-transformer-vs-full-context-8a1bc29317-20260524T135816867677+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `33`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: BPE-tokenized WikiText HMT vs parameter-matched mini-GPT confirmation: enoch://control-plane/projects/bpe-tokenized-wikitext-hmt-vs-parameter-matched-mini-gpt-c-3181a9e2e7/runs/bpe-tokenized-wikitext-hmt-vs-parameter-matched-mini-gpt-c-3181a9e2e7-20260524T103251185680+0000
- Parent run decision: Parameter-matched mini-GPT-2 HMT language-model validation: enoch://control-plane/projects/parameter-matched-mini-gpt-2-hmt-language-model-validation-8032a50ebc/runs/parameter-matched-mini-gpt-2-hmt-language-model-validation-8032a50ebc-20260524T102240224648+0000

## What looked useful

Full causal attention achieved the best mean best-validation loss: 5.3785 versus 5.3981 for segmented attention and 5.3974 for sliding local attention. At the final 1500-step checkpoint, both local variants overfit more severely than full attention.

## Boundaries and scale limits

This is bounded local validation, not a GPT-2-small-class or full WikiText-103 training result. It used WikiText-2, 16.9M parameters, 1500 steps, no dropout, and checkpoint-selected best validation loss; larger corpora, stronger regularization, longer context lengths, or bigger models could change the result.

## Claim scope

On WikiText-2 raw text tokenized with a 16k byte-level BPE, 16.9M-parameter mini-GPT models trained for 1500 optimizer steps at sequence length 256 and batch size 32 across seeds 1, 2, and 3 showed no validation advantage for segmented 64-token causal attention over full causal attention. A sliding 64-token local attention ablation also did not beat full attention.

## Why it stopped

Direct bounded validation with fixed seeds, a real full-attention baseline, and a local-window control failed to support the segmented local-attention hypothesis.

## Recommended next action

Stop this follow-up as no-paper evidence: under the bounded direct WikiText-2 BPE validation, segmented local attention did not improve validation loss over the full-context baseline.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/segmented-local-attention-mini-transformer-vs-full-context-8a1bc29317`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
