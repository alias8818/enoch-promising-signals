# Hidden-State Lookup Self-Draft on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hidden-state-lookup-self-draft-on-gb10-c033ac02a3d5`
Run ID: `hidden-state-lookup-self-draft-on-gb10-c033ac02a3d5-20260620T095342842666+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/198a2f451250

## What looked useful

Best 20k-state layer -2 run reached 0.2148 accepted tokens per 4-token draft and 19.53% first-token acceptance versus 0.1289 and 10.55% for token-context backoff; the 80k confirmation reached 0.1836 and 16.02%. Full 4-token acceptance was 0% in all non-smoke runs.

## Boundaries and scale limits

Tested only distilgpt2, WikiText-2, greedy decoding, up to 80k hidden-state datastore entries, 512 held-out prompts, and horizon 4. No end-to-end speculative decoder, larger model, sampling verifier, learned scorer, ANN index, or tree drafter was evaluated.

## Claim scope

On distilgpt2 with held-out WikiText-2 greedy verification, a naive hidden-state kNN continuation table slightly improves first-token draft acceptance over cheap token-context retrieval, but does not produce practical multi-token speculative drafts.

## Why it stopped

Bounded local evidence supports only a weak mechanism signal; naive lookup did not achieve any full 4-token draft acceptance and is not viable as a standalone speculative decoder.

## Recommended next action

Stop this no-paper run; a follow-up should test whether multi-neighbor hidden-state trees or a learned scorer can convert the weak first-token signal into practical multi-token acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hidden-State Multi-Neighbor Tree Drafting
- Success threshold: At least 0.75 mean accepted tokens per 4-token proposal and at least 5% full 4-token acceptance on >=512 held-out GPT-2-small-class prompts, with overhead low enough to plausibly beat standard greedy decoding.
- Stop condition: Stop if top-k tree lookup remains below 0.35 mean accepted tokens per proposal or produces 0% full-horizon acceptance on the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-lookup-self-draft-on-gb10-c033ac02a3d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
