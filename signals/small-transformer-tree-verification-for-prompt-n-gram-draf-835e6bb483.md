# Small-Transformer Tree Verification for Prompt N-gram Drafts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-tree-verification-for-prompt-n-gram-draf-835e6bb483`
Run ID: `small-transformer-tree-verification-for-prompt-n-gram-draf-835e6bb483-20260524T005255544683+0000`

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

- Parent run decision: Token-Tree Verification for Prompt N-gram Drafts: enoch://control-plane/projects/token-tree-verification-for-prompt-n-gram-drafts-a51965f891e9/runs/token-tree-verification-for-prompt-n-gram-drafts-a51965f891e9-20260524T003754297165+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7818fde4346a

## What looked useful

Two direct runs showed consistent exact top-1 lift over n-gram frequency (about +0.011 to +0.012 absolute) and prefix-length lift (about +0.088 to +0.090 characters/path), but both missed the pre-run useful-signal threshold of +0.10 prefix characters/path.

## Boundaries and scale limits

Single corpus, character tokens, 4-character draft paths, prompt window 512, branch cap 16, 1200 held-out positions, tiny verifier trained from scratch on CPU; no BPE tokens, pretrained target model, tree speculative decoding speedup, or multi-corpus robustness tested.

## Claim scope

In a character-level War and Peace held-out test with prompt-local n-gram draft trees, a 251k-parameter causal transformer verifier slightly improves candidate selection over raw n-gram frequency, but the improvement is below the pre-registered Tier 1 prefix-lift threshold.

## Why it stopped

Controlled small direct evidence was mixed: the verifier beat n-gram controls but did not meet the pre-registered Tier 1 prefix-lift threshold, and the character-level setup is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded BPE/pretrained-transformer target test measuring exact tree acceptance and wall-clock target-call reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE Transformer-Target Verification for Prompt N-gram Draft Trees
- Success threshold: Small verifier improves accepted BPE tokens per target call by at least 10% over raw n-gram ranking and reduces projected target calls without verifier overhead exceeding saved target work on the bounded setup.
- Stop condition: Stop if BPE true-path coverage is below 5% for practical branch caps or if verifier ranking fails to beat raw n-gram ranking on accepted-token length across two tested tree depths.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-tree-verification-for-prompt-n-gram-draf-835e6bb483`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
